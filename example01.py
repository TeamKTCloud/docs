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

endPoint='https://api.ucloudbiz.olleh.com/server/v1/client/api?'

root = db.reference()
key = root.child('User').child('KT').child('Key').get()

params={}
params['command']='listVirtualMachines'
params['state']='Running'
params['response']='json'
params['apiKey'] = key['API_KEY']    
secretkey = key['SECRET_KEY']  
secretkey = secretkey.encode('utf-8')

requestParams = '&'.join(['='.join([k,urllib.parse.quote_plus(params[k])]) for k in params.keys()])

# signature 생성
message = '&'.join(['='.join([k.lower(),urllib.parse.quote_plus(params[k]).lower()]) for k in sorted(params.keys())])
message = message.encode('utf-8')
digest = hmac.new(secretkey, msg=message, digestmod=hashlib.sha1).digest()
signature = base64.b64encode(digest)
signature = urllib.parse.quote_plus(signature)

# Request URL 생성
requestURL=endPoint+requestParams+'&signature='+signature

# print(requestURL)

# data 파싱
data = requests.get(requestURL).json()
# print(data)

# 예제 - 현재 Zone 에서 Running 상태인 vm의 수
# print(data['listvirtualmachinesresponse']['count'])
# print(data['listvirtualmachinesresponse']['virtualmachine'][0]['created'])

count = data['listvirtualmachinesresponse']['count']

dic = dict()

for i in range(count):
    name = data['listvirtualmachinesresponse']['virtualmachine'][i]['displayname']
    state = data['listvirtualmachinesresponse']['virtualmachine'][i]['state']
    created = data['listvirtualmachinesresponse']['virtualmachine'][i]['created']
    cupspeed = data['listvirtualmachinesresponse']['virtualmachine'][i]['cpuspeed']
    dic[name] = {'State':state, 'Created':created, 'CpuSpeed':cupspeed}
    # root = db.reference()   
    root.child('User').child('KT').child('Resources').child('VM').update(dic)



# mnjv4D2hZAnMgik0Lej36V8qDiOca_zV78mCqHpD5hUqxzDoxPkI2xHF8ifL4YrqGWIJUuqAr2MC-cMLXRW8fw
# w32U6OFJlmsPmfLgCdlIhfrXcM_2ApUoz2KkLwoKTTYLdI9DO4E2A4y-MB73_P0uUc42F08osJMcDyNWStwvRQ

# https://api.ucloudbiz.olleh.com/server/v1/client/api?apikey=mnjv4D2hZAnMgik0Lej36V8qDiOca_zV78mCqHpD5hUqxzDoxPkI2xHF8ifL4YrqGWIJUuqAr2MC-cMLXRW8fw&command=listVirtualMachines&name&state=running&response=json&signature=BYm8YZUQ%2FzyRlV4nT2x1yW5Alcs%3D
# https://api.ucloudbiz.olleh.com/server/v1/client/api?apikey=mnjv4D2hZAnMgik0Lej36V8qDiOca_zV78mCqHpD5hUqxzDoxPkI2xHF8ifL4YrqGWIJUuqAr2MC-cMLXRW8fw&command=listVirtualMachines&name&state=running&response=json&signature=BYm8YZUQ%2FzyRlV4nT2x1yW5Alcs%3D