'''
@author: ssolly
'''

import requests
import json 


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
    
    
    def make_word_to_define_dictionary(self):
        '''Take all the xords to define and put them in a dictionary
        '''
        word_dict = {}
        for word in self.words_to_define:
            word_dict[word] = ''
        return word_dict
    

    def make_api_request(self):
        '''Make api request with each url
        @return list with all requested object
        '''
        all_urls = self.make_urls()
        print('This is my urls:',all_urls)
        request_list =[]
        for url in all_urls:
            request_list.append(requests.get(url, headers = {'app_id':self.api_parameters['api_id'], 'app_key':self.api_parameters['api_key']}))
        return request_list
    
    
    def make_words_dict(self):
        '''Make a dictionary with all words
        @return dictionary with all words 
        '''
        requested_urls = self.make_api_request()
        print('This are the requested urls', requested_urls)
        json_data = []
        for req_url in requested_urls:
            if req_url.status_code ==200:
                json_data.append(json.loads(req_url.text))
                
        return json_data
    
    def set_definitions(self):
        '''Set definitons of my dictionary words
        '''
        json_data = self.make_words_dict()
        non_def_dict = self.make_word_to_define_dictionary()
        
        for index in range (len(json_data)):
            for syno_dict in json_data[index]['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']:
                non_def_dict[json_data[index]['results'][0]['word']]=syno_dict['id']
        for key in non_def_dict.keys():
            if non_def_dict[key]=='':
                del non_def_dict[key]
                
        return non_def_dict
        


            
            
            
            
            
            
            
