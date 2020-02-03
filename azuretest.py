import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import hashlib
import hmac
import base64
import requests
import urllib

cred = credentials.Certificate('./example01-c1e3e-firebase-adminsdk-qi6cv-2975ba173f.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://example01-c1e3e.firebaseio.com/'})

root = db.reference()
key = root.child('User').child('Azure').child('Key').get()

# Tenant ID for your Azure subscription //Directory
TENANT_ID = key['TENANT_ID']

# Your service principal App ID
CLIENT = key['CLIENT']

# Your service principal password
KEY = key['KEY']


subscription_id = key['subscription_id']

credentials = ServicePrincipalCredentials(
    client_id = CLIENT,
    secret = KEY,
    tenant = TENANT_ID
)

compute_client = ComputeManagementClient(credentials, subscription_id)

dic = dict()

print('\nList VMs in resource group')
for vm in compute_client.virtual_machines.list_all():
    print("\tVM: {}".format(vm.name))
name = format(vm.name)

dic[name] = {'State':'Running'}

root.child('User').child('Azure').child('Resources').child('VM').update(dic)