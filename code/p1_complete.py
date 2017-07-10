# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 17:58:51 2016

@author: Qiyue
"""

import json
import datetime, time
import numpy as np
import matplotlib.pyplot as plt


f = open('tweet_data/tweets_#patriots.txt')

line = f.readline()

#import json
tweet = json.loads(line)

tweet['tweet']['text']
start_date = datetime.datetime(2015,01,18, 0,0,0)
mintime = int(time.mktime(start_date.timetuple()))


ntweets_hour = [0]*504 # list of number of tweets for each hour: 0->1, 1->2, ... 23->24
sum_followers = 0.
sum_users = 0.
sum_retweets = 0.
sum_tweets = 0.
while len(line)!=0:
    tweet = json.loads(line)
    current_date = tweet['firstpost_date']
    #tweet_datetime = datetime.datetime.fromtimestamp(tweet['firstpost_date'])	
    if current_date>=mintime:
        ihour = (tweet['firstpost_date']-mintime)/3600
        ntweets_hour[ihour] += 1
    
    
    # number of followers of the current user posting the tweet
        nfollowers = int(tweet['tweet']['user']['followers_count'])
        sum_followers += nfollowers
        sum_users += 1.0				
				
				# number of retweets
        n_retweets = tweet['metrics']['citations']['total']
        sum_retweets += n_retweets
        sum_tweets += 1.0
        #tweets.append(tweet)
    line = f.readline()
    
print 'average number of tweets per hour is %f' % (np.mean(ntweets_hour))	
print 'average number of followers of users posting the tweets is %f' % (sum_followers/sum_users)
print 'average number of retweets for is %f' % (sum_retweets/sum_tweets)
print '\n'

#ypos = np.arange(len(ntweets_hour))
#plt.bar(ypos,ntweets_hour)
#plt.title('superbowl')
#plt.xlabel('hour')
#plt.ylabel('number of tweets in hour')
#fig = plt.gcf()
#fig.set_size_inches(10,8)
#fig.savefig('superbowl', dpi=100)
#plt.show()



#start_date = datetime.datetime(2015,01,01, 12,0,0)
#end_date = datetime.datetime(2015,02,01, 15,0,0)
#mintime = int(time.mktime(start_date.timetuple()))
#maxtime = int(time.mktime(end_date.timetuple()))
#
#
#num_tweets = len(tweets)
#num_window = 0
#
#max_followers = 0
#for i in range(0, num_tweets):
#    tweet = tweets[i]
#    tweet_time = tweet['firstpost_date']
#    if tweet_time >= mintime:
#        if tweet_time >= maxtime:
#            break;
#        num_window += 1
#        max_followers = max(max_followers, tweet['tweet']['user']['followers_count'])
    


