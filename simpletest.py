'''
@author: ssolly
'''

import requests
import json 
from collectWords import CollectWords




'''app_id = '1bc5f20b'
app_key = 'fe800acc932e1b79ab4bed69ae13d208'

language = 'en'
word_id = 'torch'

url = 'https://od-api.oxforddictionaries.com/api/v1/entries/' + language + '/' + word_id.lower() + '/synonyms'

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
print(r.status_code)
json_data= json.loads(r.text)

print(type(json_data))
print(json_data)

for key, value in json_data.items():
    print (key,value)

for syno_dict in  json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']:
    print(syno_dict['id'])

print (json_data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms'])
#print(' '+json_res['results'])'''

class ApiCallManager(object):
    '''Manage OxfordDictionary api call
    '''
    def __init__(self, words_to_define, api_dict):
        '''
        @param words_to_define: list of word to Define
        @param api_dict: dictionary with api parameters
        '''
        self.words_to_define = words_to_define
        self.api_parameters = {'url': api_dict['url'], 'language': api_dict['language'], 'api_id': api_dict['api_id'], 'api_key':api_dict['api_key'], 'word_id': words_to_define}
    
    def make_urls(self):
        '''Make a list with all urls of all words to define
        @return list of urls 
        '''
        url_list = []
        for word in self.words_to_define:
            
            url_list.append(self.api_parameters['url']+self.api_parameters['language']+'/'+word.lower()+'/synonyms')
        
        return url_list
    
    def make_api_request(self):
        '''Make api request with each url
        @return list with all requested object
        '''
        all_urls = self.make_urls()
        print('This is my urls:',all_urls)
        request_list =[]
        for url in all_urls:
            request_list.append(requests.get(url, headers = {'api_id':self.api_parameters['api_id'], 'app_key':self.api_parameters['api_key']}))
        return requests
    
    
    
    def make_words_dict(self):
        '''Make a dictionary with all words
        @return dictionary with all words 
        '''
        requested_urls = self.make_api_request()
        print('This are the requested urls', requested_urls)
        json_data = []
        words_dict = {}
        print('This is the type of the requested_urls', type(requested_urls))
        for req_url in requested_urls:
            if req_url.status_code ==200:
                json_data.append(json.loads(req_url.text))
                words_dict.pop(json_data['results'][0]['word'])
        print('This are the words', words_dict)
        return words_dict
 
instance0 = CollectWords('refWords.txt','test_txt.txt')
word_id = instance0.parse_text()
#print(a)
#print(len(a))'''              
           
api_dict = {'url':'https://od-api.oxforddictionaries.com/api/v1/entries/', 'language':'en', 'api_id': '1bc5f20b', 'api_key': 'fe800acc932e1b79ab4bed69ae13d208', 'word_id':word_id }
instance = ApiCallManager(word_id,api_dict)
words_dict = instance.make_words_dict()
print('This is the dict',words_dict)
            
            
            
            
            
            
            