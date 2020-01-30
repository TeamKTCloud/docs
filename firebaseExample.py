import firebase_admin
from firebase_admin import credentials
cred = credentials.Certificate('./YOUR_firebase.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://YOURPROJECT.firebaseio.com/'})

dic = dict()
dic['posco stock'] = {'title':"posco article6", 'up_down': str(probList), 'key_prob': str(lime_list), 'contents':input_text, 'links':'http://www.google.com'}

from firebase_admin import db
root = db.reference()
root.child('stock').update(dic)