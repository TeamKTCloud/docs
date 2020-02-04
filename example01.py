import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
import boto3
import botocore
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import hashlib
import hmac
import base64
import requests
import urllib
import sys


cred = credentials.Certificate('./example01-c1e3e-firebase-adminsdk-qi6cv-2975ba173f.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://example01-c1e3e.firebaseio.com/'})

VM_endPoint='https://api.ucloudbiz.olleh.com/server/v1/client/api?'
LB_endPoint = 'https://api.ucloudbiz.olleh.com/loadbalancer/v1/client/api?'
root = db.reference()


#KT
class KT_instance():
    key = root.child('User').child('KT').child('Key').get()
    requestURL = 0
    data = 0
    command_list = 0
    command = 0
    requestParams = 0
    
    def CreateURL(self, command):
        self.command = command
        params={}
        params['command']=self.command
        params['response']='json'
        params['apiKey'] = self.key['API_KEY']    
        secretkey = self.key['SECRET_KEY']  
        secretkey = secretkey.encode('utf-8')
        self.requestParams = '&'.join(['='.join([k,urllib.parse.quote_plus(params[k])]) for k in params.keys()])

        # signature 생성
        message = '&'.join(['='.join([k.lower(),urllib.parse.quote_plus(params[k]).lower()]) for k in sorted(params.keys())])
        message = message.encode('utf-8')
        digest = hmac.new(secretkey, msg=message, digestmod=hashlib.sha1).digest()
        signature = base64.b64encode(digest)
        signature = urllib.parse.quote_plus(signature)

        # Request URL 생성
        if self.command == 'listVirtualMachines':
            self.requestURL=VM_endPoint+self.requestParams+'&signature='+signature
            # print(self.requestURL)
        if self.command == 'listLoadBalancers':
            self.requestURL=LB_endPoint+self.requestParams+'&signature='+signature
            # print(self.requestURL)

    def DataParsing(self):
        # data 파싱
        self.data = requests.get(self.requestURL).json()
        # print(self.data)

    def DataPut(self):
        dic = dict()
        if self.command == 'listVirtualMachines':
            count = self.data['listvirtualmachinesresponse']['count']
            for i in range(count):
                name = self.data['listvirtualmachinesresponse']['virtualmachine'][i]['displayname']
                state = self.data['listvirtualmachinesresponse']['virtualmachine'][i]['state']
                created = self.data['listvirtualmachinesresponse']['virtualmachine'][i]['created']
                cupspeed = self.data['listvirtualmachinesresponse']['virtualmachine'][i]['cpuspeed']
                dic[name] = {'State':state, 'Created':created, 'CpuSpeed':cupspeed}
                root.child('User').child('KT').child('Resources').child('VM').update(dic)

        if self.command == 'listLoadBalancers':
            count = self.data['listloadbalancersresponse']['count']
            for i in range(count):
                name = self.data['listloadbalancersresponse']['loadbalancer'][i]['name']
                id = self.data['listloadbalancersresponse']['loadbalancer'][i]['loadbalancerid']
                state = self.data['listloadbalancersresponse']['loadbalancer'][i]['state']
                dic[name] = {'ID':id, 'State':state}
                root.child('User').child('KT').child('Resources').child('LB').update(dic)


#AWS
class AWS_instance():
    key = root.child('User').child('AWS').child('Key').get()
    ec2_client = 0 
    ec2_resource = 0
    response = 0


    def CreateKey(self):
        self.ec2_client = boto3.client(
            'ec2',
            # Hard coded strings as credentials, not recommended.
        aws_access_key_id = self.key['aws_access_key_id'],
        aws_secret_access_key = self.key['aws_secret_access_key'],
        region_name = self.key['region_name']
        )

        self.ec2_resource = boto3.resource(
            'ec2',
            # Hard coded strings as credentials, not recommended.
            aws_access_key_id = self.key['aws_access_key_id'],
            aws_secret_access_key = self.key['aws_secret_access_key'],
            region_name = self.key['region_name']
        )

    def DataPut(self):
        dic = dict()
        self.response = self.ec2_client.describe_instances()
        i = 0
        while i < len(self.response):
            name = self.response['Reservations'][i]['Instances'][0]['Tags'][0]['Value']
            isinstance_id = self.response['Reservations'][i]['Instances'][0]['InstanceId']
            state = self.response['Reservations'][i]['Instances'][0]['State']['Name']
            print(name, state, isinstance_id)
            dic[name] = {'State' : state}
            root.child('User').child('AWS').child('Resource').child('VM').update(dic)
            i = i+1


#Azure
class Azure_instance():
    key = root.child('User').child('Azure').child('Key').get()
    compute_client = 0

    def CreateKey(self):
        TENANT_ID = self.key['TENANT_ID']
        CLIENT = self.key['CLIENT']
        KEY = self.key['KEY']
        subscription_id = self.key['subscription_id']
        credentials = ServicePrincipalCredentials(
            client_id = CLIENT,
            secret = KEY,
            tenant = TENANT_ID
            )
        self.compute_client = ComputeManagementClient(credentials, subscription_id)

    
    def DataPut(self):
        dic = dict()
        for vm in self.compute_client.virtual_machines.list_all():
            print("\tVM: {}".format(vm.name))
        name = format(vm.name)
        dic[name] = {'State':'Running'}
        root.child('User').child('Azure').child('Resources').child('VM').update(dic)


# #'listVirtualMachines', 'listLoadBalancers', 'usageLoadBalancerService'
KT_instance = KT_instance()

# #listVirtualMachines
KT_instance.CreateURL('listVirtualMachines')
KT_instance.DataParsing()
KT_instance.DataPut()

# #listLoadBalancers
KT_instance.CreateURL('listLoadBalancers')
KT_instance.DataParsing()
KT_instance.DataPut()

AWS_instance = AWS_instance()
AWS_instance.CreateKey()
AWS_instance.DataPut()

Azure_instance = Azure_instance()
Azure_instance.CreateKey()
Azure_instance.DataPut()


