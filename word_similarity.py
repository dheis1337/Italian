import pandas as pd
import numpy as np
from difflib import SequenceMatcher

# read in words
anki = pd.read_csv('~/MyStuff/DataScience/Italian/italianexport.csv')


# take first column
words = list(anki.iloc[:,0])


# create dictionary of elements
letter_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8,
               'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16,
               'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 
               'y':24, 'z':25, 'è':4, 'ì':8, 'ò':14, 'ù':20, 'é':4, 'à':0}
               


letter_dict.keys() 

vector_dict = {}
for i in range(len(words)):
    letter_vec = np.zeros(26)
    letters = list(words[i])
    letter_locs = [letter_dict[letter] for letter in letters]
    letter_vec[letter_locs] = 1
    new_ele = {words[i]:letter_vec}
    vector_dict.update(new_ele)        
    


alpha_words = sorted(words)


alpha_words.index('b*')

next(enumerate((word for word in alpha_words if word.startswith('c'))), None)

alpha_words.startswith('a')

[word for words in alpha_words if word.startswith('a')]


a_list = list(filter(lambda x: x[0] == 'a', alpha_words))


words.index('veloce')


alpha_array = np.array(alpha_words)
np.where(alpha_array)


loc_dict = {}
for j in range(len(letters)):    
    temp_dict = {}
    words = [i for i in alpha_words if i[0] == 'a']        
    letter_loc = [[words[0], words[len(words) - 1]]
    temp_dict = {letters[i]:letter_loc}
    loc_dict.update(letter_dict)
    

    
    
words = [i for i in alpha_words if i[0] == 'a']
[i for i in alpha_words if i[0] == 'a'][len(words) - 1]

     

range(set(0, 1))
min([i for i, item in enumerate(alpha_array) if item.startswith('c')])



SequenceMatcher(None, 'veloce', 'veloce').ratio()




