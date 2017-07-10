# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 15:19:23 2016

@author: Qiyue
"""

import numpy as np
import statsmodels.api as sm
import json
import pickle
import datetime, time

f = open('test_data/sample2_period2.txt')

line = f.readline()

#import json
tweet = json.loads(line)
tag1 = '#gohawks'
tag1_2 = '#seahawks'
tag1_3 = '#seattle'
tag2 = '#gopatriots'
tag2_2 = '#patriots'

hawks = 0
patriots = 0

while len(line)!=0:
    tweet = json.loads(line)

    if (tag1 in (tweet['highlight']).lower() or tag1_2 in (tweet['highlight']).lower() or tag1_3 in (tweet['highlight']).lower()) and not(tag2 in (tweet['highlight']).lower() or tag2_2 in (tweet['highlight']).lower()):
        hawks+=1;

        
    else:
        if (tag2 in (tweet['highlight']).lower() or tag2_2 in (tweet['highlight']).lower()) and not(tag1 in (tweet['highlight']).lower() or tag1_2 in (tweet['highlight']).lower() or tag1_3 in (tweet['highlight']).lower()):
           patriots+=1

    line = f.readline()
    
print hawks
print patriots
