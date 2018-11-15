import numpy as np
import pandas as pd
import codecs


# read in anki deck
anki = pd.read_csv('C:/MyStuff/DataScience/Projects/Italian/italianexport.csv')

# store in list
words = list(anki.iloc[:, 0])

########################### Clean words list ##################################
words = [word.replace('li ', '') for word in words]
words = [word.replace('lo ', '') for word in words]
words = [word.replace('da ', '') for word in words]
words = [word.replace('un ', '') for word in words]
words = [word.replace('una ', '') for word in words]
words = [word.replace('uno ', '') for word in words]
words = [word.replace('il ', '') for word in words]
words = [word.replace('la ', '') for word in words]
words = [word.replace('gli ', '') for word in words]
words = [word.replace('a ', '') for word in words]
words = [word.replace('l\'', '') for word in words]
words = [word.replace('i ', '') for word in words]

# read in dictionary
with open('C:/MyStuff/DataScience/Projects/Italian/cmogcbdsdk-1488719198-ea5a65.txt', encoding = 'utf-8') as f:
    lines = f.readlines()
        
############################## Begin cleaning of line #########################
# split the list of strings into a nested list where each element is a word
# and it's associated information
lines = [line.split() for line in lines]

# find all the words in the dictionary that I have in my anki deck
word_dict = []
for word in words:
    word_dict.append([line for line in lines if word in line])

    
# remove empty entries from the nested liste
word_dict = [line for line in word_dict if line != []]

# flatten word_dict
flat_dict = [line for sublist in word_dict for line in sublist]

# separate nouns 
nouns = [line for line in flat_dict if 'noun' in line]

# separate adjectives
adj = [line for line in flat_dict if 'adj' in line]

# separate verbs
verbs = [line for line in flat_dict if 'verb' in line]

# separate adverbs
adv = [line for line in flat_dict if 'adv' in line]

