import pandas as pd
import numpy as np
from difflib import SequenceMatcher
import itertools

# read in words
anki = pd.read_csv('~/MyStuff/DataScience/italian/italianexport.csv')


# take first column
words = list(anki.iloc[:,0])


# create all 2-pair combinations of the elements of words
combos = list((itertools.combinations(words, 2)))

# create an empty dictionary to put the scores in
match_ratio = []

# loop through combos and compute the ratio of similarity between each pair
for pair in combos:
    match_ratio.append(SequenceMatcher(None, pair[0], pair[1]).ratio())
    

# zip the combos list and the match_ratio list into one dictionary
match_dict = dict(zip(combos, match_ratio))

# sort the dictionary so greatest values are towards the top
sorted_match = sorted(match_dict.items(), key = lambda x: x[1], reverse = True)










