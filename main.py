'''
Created on 9 oct. 2017

@author: ssolly
'''
from simpletest import ApiCallManager
from collectWords import CollectWords

def main():
    '''The main function'''
    autoDict = CollectWords('refWords.txt','test_txt.txt')
    word_id = autoDict.parse_text()
    api_dict = {'url':'https://od-api.oxforddictionaries.com/api/v1/entries/', 'language':'en', 'api_id': '1bc5f20b', 'api_key': 'fe800acc932e1b79ab4bed69ae13d208', 'word_id':word_id }
    instance = ApiCallManager(word_id, api_dict)
    dicti = instance.set_definitions()
    print(dicti)


if __name__=='__main__':
    main()