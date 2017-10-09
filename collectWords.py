'''
Created on 5 oct. 2017

@author: ssolly
'''
import os


def strip_list(list_of_words):
    '''
    Strip list of words before anything
    '''
    striped_list=[]
    car_list = ['.', ',', ';', ':', ' ']
    
    for car in car_list:
        for word in list_of_words:
            if car in word:
                striped_list.append(word.strip(car))
    
    return striped_list


def get_normal_words(all_words):
    '''
    '''
    car_list = ['.', ',', ';', ':', ' ']
    for car in car_list:
        for i, word in enumerate(all_words):
        
            if car in word:
                del all_words[i]
    
    return all_words


def set_final_list_words(striped_words_list, normal_words_list):
    '''
    '''
    return striped_words_list+normal_words_list


class CollectWords(object):
    '''This class will read a pdf file and collect all 
    words which are not present in refWords
    '''
    def __init__(self, ref_file_name, book_file, logger_in=None):
        '''Init CollectWords
        @param pdf_file: pdf file to read
        @param logger_in: logger
        '''
        self.logger = logger_in
        self.the_file = ref_file_name
        self.the_book = book_file
    
    def read_ref_file(self):
        '''Read the reference file 
        @return list with all reference words
        '''
        file_to_read = self.the_file
        if not os.path.isabs(file_to_read):
            file_to_read = os.path.abspath(self.the_file)
        if os.path.exists(file_to_read) is False:
            raise Exception('Can not open this file {filename}'.format(filename=file_to_read))
        refWords_list=[]
        fp = open(file_to_read)
        for line in fp:
            refWords_list.append(line.strip('\n'))
            
        return refWords_list
    
    def read_book(self):
        '''Read the book
        '''
        file_to_read = self.the_book
        if not os.path.isabs(file_to_read):
            file_to_read = os.path.abspath(self.the_book)
        if os.path.exists(file_to_read) is False:
            raise Exception('Can not open this file {filename}'.format(filename=file_to_read))
        fp = open(file_to_read)
        return fp

    
    def parse_text(self):
        '''Parse the text '''
        
        fp = self.read_book()
        reflist = strip_list(self.read_ref_file())
        text_lines = []
        word_from_text = []
        text_words = []
        word_to_define = []
        
        #construire liste contenant les phrases
        for line in fp:
            text_lines.append(line.strip('\n'))
        
        #print(text_lines)
        for line in text_lines:
            word_from_text.append(line.split())
        #Construction liste finale contenant les mots provenant du text
        for sublist in word_from_text:
            for word in sublist:
                text_words.append(word.strip('.'))
        print(len(text_words))
        ntexwords = strip_list(text_words)
        normal_words = get_normal_words(text_words)
        final_words = set_final_list_words(ntexwords, normal_words)
        
        for text_word in final_words:
            text_word.lower()
            if text_word not in reflist and text_lines not in word_to_define :
                
                print('{word}: is not in the dictionary '.format(word =text_word))
                word_to_define.append(text_word) 
            else:
                print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                print('{word}: FOUND IN THE dictionary'.format(word =text_word))
                print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                  
        return word_to_define
                    
            
        
        
        

            
        
        