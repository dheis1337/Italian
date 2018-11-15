import pandas as pd
import numpy as np
import random
import itertools

# this script is a program that will generate a math problem using two numbers. 
# the question will be posed using the written form of the numbers, and expects 
# the written form of the answer to be supplied. 

# dictionary for numbers and their associated written forms
num_dict = {'uno':1, 'due':2, 'tre':3, 'quattro':4, 'cinque':5, 'sei':6, 'sette':7,
            'otto':8, 'novo':9, 'dieci':10, 'undici':11, 'dodici':12, 'tredici':13,
            'quattrodici':14, 'quindici':15, 'sedici':16, 'diciassette':17, 'diciotto':18,
            'diciannove':19, 'venti':20, 'ventuno':21, 'ventidue':22, 'ventitre\'':23, 
            'ventiquattro':24, 'venticinque':25, 'ventisei':26, 'ventisette':27, 'ventotto':28,
            'ventinove':29, 'trenta':30, 'trentuno':31, 'trentadue':32, 'trentatre\'':33,
            'trentaquattro':34, 'trentacinque':35, 'trentasei':36, 'trentasette':37, 
            'trentotto':38, 'trentanove':39, 'quaranta':40, 'quarantuno':41, 'quarantadue':42, 'quarantatre\'':43,
            'quarantaquattro':44, 'quarantacinque':45, 'quarantasei':46, 'quarantasette':47,
            'quarantotto':48, 'quanrantanove':49, 'cinquanta':50, 'cinquantuno':51, 
            'cinquantadue':52, 'cinquantre\'':53, 'cinquantaquattro':54, 'cinquantacinque':55,
            'cinquantasei':56, 'cinquantasette':57, 'cinquantotto':58, 'cinquantanove':59,
            'sessanta':60, 'sessantuno':61, 'sessantadue':62, 'sessantatre\'':63, 'sessantaquattro':64,
            'sessantacinque':65, 'sessantasei':66, 'sessantasette':67, 'sessantotto':68, 
            'sessantanove':69, 'settanta':70, 'settantuno':71, 'settantadue':72, 
            'settantatre\'':73, 'settantaquattro':74, 'settantacinque':75, 'settantasei':76,
            'settantasette':77, 'settantotto':78, 'settantanove':79, 'ottanta':80,
            'ottantuno':81, 'ottantadue':82, 'ottantatre\'':83, 'ottantaquattro':84, 
            'ottantacinque':85, 'ottantasei':86, 'ottantasette':87, 'ottantotto':88,
            'ottantanove':89, 'novanta':90, 'novantuno':91, 'novantadue':92, 'novantatre\'':93,
            'novantaquattro':94, 'novantacinque':95, 'novantasei':96, 'novantasette':97,
            'novantotto':98, 'novantanove':99, 'cento':100}

num_dict.update({v: k for k, v in num_dict.items()})

# create a score dict using all the keys in the num_dict and a value that is a 
# 3 element np array.
score_dict = {k:np.zeros(3) for k in num_dict.keys()}

# this while loop is the main program that asks for either the number associated 
# with a written number, or vice-versa. n can be set to have the program run 
# as many times as you'd like. 
runs = 10
i = 0
while i <= runs:
    scores = list(score_dict.items())
    scores.sort(key = lambda x: x[1][2], reverse = False)
    
    # select a random number from an exponential distribution. This will allow 
    # me to be selecting the worst scores more frequently. If the randomly
    selection = round(np.random.exponential(len(num_dict) / 3))
    
    # get the key
    key = scores[selection][0]
        
    # get the value associated with the specific key
    key_val = num_dict[key]
    
    if type(key_val) == int:
        answer_in = str(input(str(key_val) + ' is written as: '))
        if answer_in == key:
            print('Correct!')
            i += 1
        
            ##############  update the scoring dictionary #####################
            # read in n (correct answers) and N (number of attempts)
            n = score_dict[key][0] 
            N = score_dict[key][1] 
        
            # add one to n and N
            n += 1
            N += 1

            # update the scoring dictionary
            score_dict[key][0] = n
            score_dict[key][1] = N
            score_dict[key][2] = n / N
      
 
        else:
            print('Incorrect :/')
            i += 1
        
            ##############  update the scoring dictionary #####################
            # read in n (correct answers) and N (number of attempts)
            n = score_dict[key][0]
            N = score_dict[key][1]
            
            # add one to N to signify another attempt, but not n since the answer
            # was incorrect            
            N += 1
            
            # update the scoring dictionary for the key 
            score_dict[key][0] = n
            score_dict[key][1] = N
            score_dict[key][2] = n / N
    else: 
        answer_in = int(input(key_val + ' is the number: '))
        if answer_in == key:
            print('Correct!')
            i += 1
        
            ##############  update the scoring dictionary #####################
            # read in n (correct answers) and N (number of attempts)
            n = score_dict[key][0] 
            N = score_dict[key][1] 
        
            # add one to n and N
            n += 1
            N += 1

            # update the scoring dictionary
            score_dict[key][0] = n
            score_dict[key][1] = N
            score_dict[key][2] = n / N
      
 
        else:
            print('Incorrect :/')
            i += 1
        
            ##############  update the scoring dictionary #####################
            # read in n (correct answers) and N (number of attempts)
            n = score_dict[key][0]
            N = score_dict[key][1]
            
            # add one to N to signify another attempt, but not n since the answer
            # was incorrect            
            N += 1
            
            # update the scoring dictionary for the key 
            score_dict[key][0] = n
            score_dict[key][1] = N
            score_dict[key][2] = n / N 


        



