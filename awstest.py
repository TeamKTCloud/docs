import boto3
import botocore
import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import requests


cred = credentials.Certificate('./example01-c1e3e-firebase-adminsdk-qi6cv-2975ba173f.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://example01-c1e3e.firebaseio.com/'})


#DB에서 키, 지역 받아오기

root = db.reference()
key = root.child('User').child('AWS').child('Key').get()

ec2_client = boto3.client(
    'ec2',
    # Hard coded strings as credentials, not recommended.
   aws_access_key_id = key['aws_access_key_id'],
   aws_secret_access_key = key['aws_secret_access_key'],
   region_name = key['region_name']
)

ec2_resource = boto3.resource(
    'ec2',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id = key['aws_access_key_id'],
    aws_secret_access_key = key['aws_secret_access_key'],
    region_name = key['region_name']
)

dic = dict()

    
# response = ec2_client.describe_instance_status(IncludeAllInstances = True)
# print(response)


# for instance in ec2_resource.instances.all():
#     print (instance.id, instance.state)


response = ec2_client.describe_instances()
# print(response)
 

name = response['Reservations'][0]['Instances'][0]['Tags'][0]['Value']
isinstance_id = response['Reservations'][0]['Instances'][0]['InstanceId']
state = response['Reservations'][0]['Instances'][0]['State']['Name']
print(name, state, isinstance_id)

# response = ec2_client.describe_volume_status()
# print(response)

dic[name] = {'State' : state}

root.child('User').child('AWS').child('Resource').child('VM').update(dic)







