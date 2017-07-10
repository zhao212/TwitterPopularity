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
#F1 = open('test_data/sample1_period1.txt')
##F2 = open('test_data/sample2_period2.txt')
##F3 = open('test_data/sample3_period3.txt')
##F4 = open('test_data/sample4_period1.txt')
##F5 = open('test_data/sample5_period1.txt')
##F6 = open('test_data/sample6_period2.txt')
##F7 = open('test_data/sample7_period3.txt')
##F8 = open('test_data/sample8_period1.txt')
##F9 = open('test_data/sample9_period2.txt')
##F10 = open('test_data/sample10_period3.txt')

#hotlevel
def gh_HL(hour):
    return {
        0: 5,
        1: 30,
        2: 30,
        3: 40,
        4: 40,
        5: 50,
        6: 125,
        7: 90,
        8: 100,
        9: 80,
        10: 40,
        11: 10,
    }[hour]
    
def gp_HL(hour):
    return {
        0: 5,
        1: 40,
        2: 40,
        3: 60,
        4: 70,
        5: 130,
        6: 350,
        7: 380,
        8: 170,
        9: 310,
        10: 330,
        11: 19,
    }[hour]
    
def nfl_HL(hour):
    return {
        0: 15,
        1: 9,
        2: 9,
        3: 11,
        4: 12,
        5: 20,
        6: 100,
        7: 80,
        8: 85,
        9: 70,
        10: 100,
        11: 5,
    }[hour]
    
def pat_HL(hour):
    return {
        0: 9,
        1: 12,
        2: 50,
        3: 45,
        4: 30,
        5: 30,
        6: 40,
        7: 30,
        8: 10,
        9: 20,
        10: 40,
        11: 3,
    }[hour]
    
def sb49_HL(hour):
    return {
        0: 3,
        1: 20,
        2: 110,
        3: 100,
        4: 70,
        5: 70,
        6: 100,
        7: 100,
        8: 90,
        9: 50,
        10: 15,
        11: 7,
    }[hour]
    
def sb_HL(hour):
    return {
        0: 9,
        1: 10,
        2: 11,
        3: 13,
        4: 15,
        5: 26,
        6: 190,
        7: 210,
        8: 270,
        9: 130,
        10: 130,
        11: 5,
    }[hour]

f = open('test_data/sample9_period2.txt')

line = f.readline()

#import json
tweet = json.loads(line)
tag1 = '#gohawks'
tag2 = '#nfl'
tag3 = '#gopatriots'
tag4 = '#patriots'
tag5 = '#sb49'
tag6 = '#superbowl'

gohawks_tweets = [0]*24 
gohawks_nfollowers = [0]*24
gohawks_retweets = [0]*24
gohawks_rs = [0]*24
gohawks_friends = [0]*24
gohawks_fav = [0]*24
gohawks_hl = [0]*24

nfl_tweets = [0]*24 
nfl_nfollowers = [0]*24
nfl_retweets = [0]*24
nfl_rs = [0]*24
nfl_friends = [0]*24
nfl_fav = [0]*24
nfl_hl = [0]*24

gop_tweets = [0]*24 
gop_nfollowers = [0]*24
gop_retweets = [0]*24
gop_rs = [0]*24
gop_friends = [0]*24
gop_fav = [0]*24
gop_hl = [0]*24

pat_tweets = [0]*24 
pat_nfollowers = [0]*24
pat_retweets = [0]*24
pat_rs = [0]*24
pat_friends = [0]*24
pat_fav = [0]*24
pat_hl = [0]*24

sb49_tweets = [0]*24 
sb49_nfollowers = [0]*24
sb49_retweets = [0]*24
sb49_rs = [0]*24
sb49_friends = [0]*24
sb49_fav = [0]*24
sb49_hl = [0]*24

sb_tweets = [0]*24 
sb_nfollowers = [0]*24
sb_retweets = [0]*24
sb_rs = [0]*24
sb_friends = [0]*24
sb_fav = [0]*24
sb_hl = [0]*24

while len(line)!=0:
    tweet = json.loads(line)
    tweet_datetime = datetime.datetime.fromtimestamp(tweet['firstpost_date'])	
    ihour = tweet_datetime.hour
    nfollowers = int(tweet['tweet']['user']['followers_count'])
    n_retweets = tweet['metrics']['citations']['total']
    rs = tweet['metrics']['ranking_score']
    num_friend = tweet['tweet']['user']['friends_count']
    n_favour = tweet['tweet']['user']['favourites_count']


    if tag1 in (tweet['highlight']).lower() or tag1_2 in (tweet['highlight']).lower():
        gohawks_tweets[ihour] += 1
        gohawks_nfollowers[ihour] += nfollowers
        gohawks_retweets[ihour] += n_retweets
        gohawks_rs[ihour] += rs      
        gohawks_friends[ihour] += num_friend   
        gohawks_fav[ihour] += n_favour
        gohawks_hl[ihour] = gh_HL(ihour - 8)
        
        
    else:
        if tag2 in (tweet['highlight']).lower():
            nfl_tweets[ihour] += 1
            nfl_nfollowers[ihour] += nfollowers
            nfl_retweets[ihour] += n_retweets
            nfl_rs[ihour] += rs      
            nfl_friends[ihour] += num_friend   
            nfl_fav[ihour] += n_favour
            nfl_hl[ihour] = nfl_HL(ihour - 8)
        else:
            if tag3 in (tweet['highlight']).lower():
                gop_tweets[ihour] += 1
                gop_nfollowers[ihour] += nfollowers
                gop_retweets[ihour] += n_retweets
                gop_rs[ihour] += rs      
                gop_friends[ihour] += num_friend   
                gop_fav[ihour] += n_favour
                gop_hl[ihour] = gp_HL(ihour - 8)
            else:
                if tag4 in (tweet['highlight']).lower():
                    pat_tweets[ihour] += 1
                    pat_nfollowers[ihour] += nfollowers
                    pat_retweets[ihour] += n_retweets
                    pat_rs[ihour] += rs      
                    pat_friends[ihour] += num_friend   
                    pat_fav[ihour] += n_favour
                    pat_hl[ihour] = pat_HL(ihour - 8)
                else:
                    if tag5 in (tweet['highlight']).lower():
                        sb49_tweets[ihour] += 1
                        sb49_nfollowers[ihour] += nfollowers
                        sb49_retweets[ihour] += n_retweets
                        sb49_rs[ihour] += rs      
                        sb49_friends[ihour] += num_friend   
                        sb49_fav[ihour] += n_favour
                        sb49_hl[ihour] = sb49_HL(ihour - 8)
                        
                    else:
                        if tag6 in (tweet['highlight']).lower():
                            sb_tweets[ihour] += 1
                            sb_nfollowers[ihour] += nfollowers
                            sb_retweets[ihour] += n_retweets
                            sb_rs[ihour] += rs      
                            sb_friends[ihour] += num_friend   
                            sb_fav[ihour] += n_favour
                            sb_hl[ihour] = sb_HL(ihour - 8)
                        else:
                            print tweet['highlight']


    line = f.readline()

def clean(a):
    b=[0]*6
    n = 0
    for i in range(len(a)):
        c=int(a[i])
        if c != 0:
            n = 1
            break
    if n == 1:
        b = [a[i],a[i+1],a[i+2],a[i+3],a[i+4],a[i+5]]
    else:
        b = [0]*6
    return b
    
gohawks_tweets = clean(gohawks_tweets)    
gohawks_nfollowers = clean(gohawks_nfollowers)   
gohawks_retweets = clean(gohawks_retweets)   
gohawks_rs = clean(gohawks_rs)   
gohawks_friends = clean(gohawks_friends)   
gohawks_fav = clean(gohawks_fav)   
gohawks_hl = clean(gohawks_hl)   

nfl_tweets = clean(nfl_tweets)   
nfl_nfollowers = clean(nfl_nfollowers)   
nfl_retweets = clean(nfl_retweets)   
nfl_rs = clean(nfl_rs)   
nfl_friends = clean(nfl_friends)   
nfl_fav = clean(nfl_fav)   
nfl_hl = clean(nfl_hl)   

gop_tweets = clean(gop_tweets)   
gop_nfollowers = clean(gop_nfollowers)   
gop_retweets = clean(gop_retweets)   
gop_rs = clean(gop_rs)   
gop_friends = clean(gop_friends)   
gop_fav = clean(gop_fav)   
gop_hl = clean(gop_hl)   

pat_tweets = clean(pat_tweets)   
pat_nfollowers = clean(pat_nfollowers)   
pat_retweets = clean(pat_retweets)   
pat_rs = clean(pat_rs)   
pat_friends = clean(pat_friends)   
pat_fav = clean(pat_fav)   
pat_hl = clean(pat_hl)   

sb49_tweets = clean(sb49_tweets)   
sb49_nfollowers = clean(sb49_nfollowers)   
sb49_retweets = clean(sb49_retweets)   
sb49_rs = clean(sb49_rs)   
sb49_friends = clean(sb49_friends)   
sb49_fav = clean(sb49_fav)   
sb49_hl = clean(sb49_hl)   

sb_tweets = clean(sb_tweets)   
sb_nfollowers = clean(sb_nfollowers)   
sb_retweets = clean(sb_retweets)   
sb_rs = clean(sb_rs)   
sb_friends = clean(sb_friends)   
sb_fav = clean(sb_fav)   
sb_hl = clean(sb_hl) 

#period 1
ghp1 = [-5.913e-07, -0.0866, 0.0001, 0.2805, 101.4762, -30.8558]

gh_pt = gohawks_nfollowers[5]*ghp1[0]+gohawks_rs[5]*ghp1[1]+gohawks_friends[5]*ghp1[2]+gohawks_tweets[5]*ghp1[3]+gohawks_hl[5]*ghp1[4]+ghp1[5]

gpp1 = [2.443e-05, 0.2572, -0.0002, -1.1456, 9.9861, 9.3022]

gp_pt = gop_nfollowers[5]*gpp1[0]+gop_rs[5]*gpp1[1]+gop_friends[5]*gpp1[2]+gop_tweets[5]*gpp1[3]+gop_hl[5]*gpp1[4]+gpp1[5]

nflp1 = [-6.618e-05,0.0388,0.0003,-0.1884,101.3320,-20.6598]
nfl_pt = nfl_nfollowers[5]*nflp1[0]+nfl_rs[5]*nflp1[1]+nfl_friends[5]*nflp1[2]+ nfl_tweets[5]*nflp1[3]+nfl_hl[5]*nflp1[4]+nflp1[5]

patp1 = [-5.483e-05,-0.5508,0.0008,2.0701,1074.7065,-5020.9593]

pat_pt = pat_nfollowers[5]*patp1[0]+pat_rs[5]*patp1[1]+pat_friends[5]*patp1[2]+ pat_tweets[5]*patp1[3]+pat_hl[5]*patp1[4]+patp1[5]

sb49p1 = [-2.878e-05,0.9854,-0.0002,-3.8932,990.0848,2531.0313]

sb49_pt = sb49_nfollowers[5]*sb49p1[0]+sb49_rs[5]*sb49p1[1]+sb49_friends[5]*sb49p1[2]+ sb49_tweets[5]*sb49p1[3]+sb49_hl[5]*sb49p1[4]+sb49p1[5]

sbp1 = [6.875e-06,0.0211,3.075e-05,-0.1803,1004.2723,-388.2178]

sb_pt = sb_nfollowers[5]*sbp1[0]+sb_rs[5]*sbp1[1]+sb_friends[5]*sbp1[2]+ sb_tweets[5]*sbp1[3]+sb_hl[5]*sbp1[4]+sbp1[5]

pt2 = sum([abs(gh_pt), abs(gp_pt), abs(nfl_pt), abs(pat_pt), abs(sb49_pt), abs(sb_pt)])
print pt2
