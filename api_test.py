'''
Created on 9 oct. 2017

@author: ssolly
'''
import requests
import json
app_id = '1bc5f20b'
app_key = 'fe800acc932e1b79ab4bed69ae13d208'

language = 'en'
word_id = 'saying'

url = 'https://od-api.oxforddictionaries.com/api/v1/entries/' + language + '/' + word_id.lower() + '/synonyms'

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
print(r.status_code)
json_data= json.loads(r.text)
for syno_dict in  json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']:
    print(syno_dict['id'])

print (json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms'])
