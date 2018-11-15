from bs4 import BeautifulSoup
import requests
from wiktionaryparser import WiktionaryParser
import pandas as pd
import numpy as np
import re

# read in words
anki = pd.read_csv('C:/MyStuff/DataScience/Projects/Italian/italianexport.csv')


# take first column
words = list(anki.iloc[:,0])


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


parser = WiktionaryParser()
word = parser.fetch(words[0], 'italian')



def word_dl(word):
    parser = WiktionaryParser()
    word = parser.fetch(word, 'italian')
    return word

wikis= [word_dl(word) for word in words]

wikis = [wiki for wiki in wikis if wiki['definitions'] != []]


wikis = [wiki[0] for wiki in wikis]




word_locs =  [i for i , wiki in enumerate(wikis) if wiki['definitions'] != []]

# make the 
found_words = np.array(words)

# 
found_words[word_locs]

wiki_dict = {definition_clean(wiki):wiki for wiki in wikis}




destra = {wiki_dict['destra\xa0f (plural destre)']['definitions'][0]['text'][0]:wiki_dict['destra\xa0f (plural destre)']}

destra[destra.keys()]



s = wikis[5]['definitions'][0]['text'][0]
t = wikis[421]['definitions'][0]['text'][0]

s.find('\xa0f')


def definition_clean(word_def):
    s = word_def['definitions'][0]['text'][0]
    if s.find('\\') == -1:
        return s
    else if s.find()
    s = s[:s.index('\xa0f')]
    




# definition(s)
word['definitions']

# pronunciations
word['pronunciations']

# IPA
word['pronunciations']['text'][0]




r = requests.get('https://en.wiktionary.org/wiki/italiano')


data = r.text

soup = BeautifulSoup(data)

# IPA
soup.select_one('.IPA').text


soup.select_one('ol li')

