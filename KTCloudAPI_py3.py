import hashlib
import hmac
import base64
import requests
import urllib

endPoint='https://api.ucloudbiz.olleh.com/server/v2/client/api?'

params={}
params['command']='listVirtualMachines'
params['state']='Running'
params['response']='json'
params['apiKey']='YOUR ACCESS KEY'
secretkey='YOUR SECRET KEY'
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

# data 파싱
data = requests.get(requestURL).json()
print(data)

# 예제 - 현재 Zone 에서 Running 상태인 vm의 수
print(data['listvirtualmachinesresponse']['count'])