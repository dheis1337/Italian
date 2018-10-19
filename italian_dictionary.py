import numpy as np
import pandas as pd
import re

# this script is for cleaning the Italian dictionary file
f = open('C:/MyStuff/DataScience/Projects/Italian/cmogcbdsdk-1488719198-ea5a65.txt')
lines = f.readlines()

# laptop file location
f = open('/home/david/MyStuff/DataScience/Italian/cmogcbdsdk-1488719198-ea5a65.txt')
lines = f.readlines()


# remove \n and \t characters
lines = [line.rstrip('\n') for line in lines]
lines = [line.replace('\t', ' ') for line in lines]

# split each list element which will make a list of sublists. Each sublist represents
# one word. 
lines = [line.split(' ') for line in lines]

# change Ã\xa0 to à and maintain nested list structure
lines = [[word.replace('Ã\xa0', 'à') for word in line] for line in lines]

# change Ã with è and maintain nested list structure
lines = [[word.replace('Ã', 'è') for word in line] for line in lines]


# Read in Anki words (Desktop)
anki = pd.read_csv('C:/MyStuff/DataScience/Projects/Italian/italianexport.csv')

# Read in Anki words (Laptop)
anki = pd.read_csv('/home/david/MyStuff/DataScience/Italian/italianexport.csv')



# make the first column (words) a list
word_list = list(anki.iloc[:, 0])

# remove articles
word_list = [word.replace('un ', '') for word in word_list]
word_list = [word.replace('una ', '') for word in word_list]
word_list = [word.replace('li ', '') for word in word_list]
word_list = [word.replace('uno ', '') for word in word_list]
word_list = [word.replace('l\'', '') for word in word_list]
word_list = [word.replace('il ', '') for word in word_list]
word_list = [word.replace('la ', '') for word in word_list]
word_list = [word.replace('lo ', '') for word in word_list]
word_list = [word.replace('i ', '') for word in word_list]


# Find all the elements in word_list that are in the dictionary list (lines)
def_list = []
for word in word_list:
    ele = (word in x for x in lines)
    indexed_ele = enumerate(ele)
    ele_indexes = (index for index, value in indexed_ele if value)
    first_ele_index = next(ele_indexes, None)
    if first_ele_index != None:       
        def_list.append(lines[first_ele_index])
    else:
        next

# clean adjectives
# find all elements with 'adj' in them
adjectives = [ele for ele in def_list if 'adj' in ele]

adj_index = [ele.index('adj') for ele in adjectives]


val_list = []
key_list = []
for i in range(len(adj_index)):
    if adj_index[i] == 2:
        val_list.append(adjectives[i][0])
        key_list.append(adjectives[i][1])
    else:
        

adjectives.index('solo')



# find all elements with 'noun' in them
nouns = [ele for ele in def_list if 'noun' in ele]

# find all the elements with 'verb' 
verbs = [ele for ele in def_list if 'verb' in ele]


