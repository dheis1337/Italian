import pandas as pd
import numpy as np
import random
import itertools

# this script is a program that will generate a math problem using two numbers. 
# the question will be posed using the written form of the numbers, and expects 
# the written form of the answer to be supplied. 

# dictionary for numbers and their associated written forms
num_dict = {'uno':1, 'due':2, 'tre':3, 'quatro':4, 'cinque':5, 'sei':6, 'sette':7,
            'otto':8, 'novo':9, 'dieci':10,
            1:'uno', 2:'due', 3:'tre', 4:'quatro', 5:'cinque', 6:'sei', 7:'sette', 
            8:'otto', 9:'novo', 10:'dieci'}


# scoring dictionary
score_dict = {1:np.zeros(3), 2:np.zeros(3), 3:np.zeros(3), 4:np.zeros(3), 5:np.zeros(3),
              6:np.zeros(3), 7:np.zeros(3), 8:np.zeros(3), 9:np.zeros(3), 10:np.zeros(3),
              'uno':np.zeros(3), 'due':np.zeros(3), 'tre':np.zeros(3), 'quatro':np.zeros(3),
              'cinque':np.zeros(3), 'sei':np.zeros(3), 'sette':np.zeros(3),
              'otto':np.zeros(3), 'novo':np.zeros(3), 'dieci':np.zeros(3)}

# this while loop is the main program that asks for either the number associated 
# with a written number, or vice-versa. n can be set to have the program run 
# as many times as you'd like. 
n = 10
i = 0
while i <= n:
    scores = list(score_dict.items())
    scores.sort(key = lambda x: x[1][2], reverse = True)
    
    # select a random number from an exponential distribution. This will allow 
    # me to be selecting the worst scores more frequently. If the randomly
    selection = round(np.random.exponential(len(num_dict) / 3))
    
    # get the key
    key = scores[selection][0]
        
    key_val = num_dict[key]
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


   
            
scores = list(score_dict.items())

scores.sort(key = lambda x: x[1][2])

np.random.choice(scores, 1, p = [.5, .25, .1, .05])


selection = round(np.random.exponential(len(num_dict) / 3))

key = scores[selection][0]




