# bag of words itwiki

import nltk
import re
import string
from nltk.corpus import wordnet as wn
import os
import matplotlib as plt
import numpy as np
import pandas as pd

# read in raw data from the sorted.it.lemma file
f = open('C:/MyStuff/DataScience/Projects/italian/sorted.it.lemma.unigrams', encoding = 'ISO-8859-1')
lines = f.readlines()

# remove new line terminator
lines = [line.rstrip('\n') for line in lines]

# remove tab delimitter
lines = [line.replace('\t', ' ') for line in lines]

# split the lines on the space between the count and token
lines = [line.split(' ') for line in lines]


# split tokens to something smaller to make it a data frame
tokens = lines[0:10000]

    
# convert to a data.frame
count_df = pd.DataFrame(np.array(tokens).reshape(-1, 2))

# set column names
count_df.columns = ['count', 'token']

# remove lines with just punctuation 
count_df = count_df[-count_df['token'].isin(list(string.punctuation))]

# remove the @card@ line because it doesn't make sense
count_df = count_df.drop([4])

# do the above for the paisa lemma txt file
# read in raw data from the sorted.it.lemma file
f = open('C:/MyStuff/DataScience/Projects/italian/lemma-frequencies-paisa.txt', encoding = 'ISO-8859-1')
paisa = f.readlines()

# remove first two elements
del paisa[0:2]


# strip out \n and \t
paisa = [line.rstrip('\n') for line in paisa]
paisa = [line.rstrip('\t') for line in paisa]

# replace ',' with a space
paisa = [line.replace(',', ' ').split(' ') for line in paisa]

# reduce size of paisa to 10000 words
paisa = paisa[0:10000]

# unlist the nested format of paisa and create two lists: tokens and counts
tokens, counts = map(list, zip(*paisa))

# create dataframe
paisa_df = pd.DataFrame(tokens, columns = ['token'])
paisa_df['counts'] = pd.Series(counts, index = paisa_df.index)

# remove lines with just punctuation 
paisa_df = paisa_df[-paisa_df['token'].isin(list(string.punctuation))]

# merge the two data frames
token_df = count_df.merge(paisa_df, on = 'token', how = 'left')

# convert nan in counts to 0 for additions
token_df['counts'] = token_df['counts'].fillna(0)

# convert count and counts to numeric
token_df[['count', 'counts']] = token_df[['count', 'counts']].apply(pd.to_numeric)

# add count and counts to get total_count
token_df['total_count'] = token_df['counts'] + token_df['count']

# drop count and counts
token_df = token_df.drop(['count', 'counts'], axis = 1)

# order by total_count
token_df = token_df.sort_values(['total_count'], ascending = False)

# save the data frame 
token_df.to_csv('C:/MyStuff/DataScience/Projects/Italian/lemma_counts.csv')

