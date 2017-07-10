# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 22:18:50 2016

@author: Qiyue
"""

#problem 3

import numpy as np
import statsmodels.api as sm
import json
import datetime, time
import matplotlib.pyplot as plt

string = 'patriots'
f = open('tweet_data/tweets_#patriots.txt')

line = f.readline()

#import json
tweet = json.loads(line)

tweet['tweet']['text']
start_date = datetime.datetime(2015,01,18, 0,0,0)
mintime = int(time.mktime(start_date.timetuple()))
end_date = datetime.datetime(2015, 2, 8,0,0,0)
maxtime = int(time.mktime(end_date.timetuple()))
nhst = datetime.datetime(2015,1,18, 1,0,0)
nhet = datetime.datetime(2015, 2, 8,1,0,0)
nhmin = int(time.mktime(nhst.timetuple()))
nhmax = int(time.mktime(nhet.timetuple()))

tweets = []
ntweets_hour = [0]*504 # list of number of tweets for each hour: 0->1, 1->2, ... 23->24
sum_followers = [0]*504
max_followers = [0]*504
#sum_users = 0.
sum_retweets = [0]*504
#sum_tweets = 0.
time_of_day = [0]*504

ranking_score = [0.]*504

sum_friends = [0.]*504
sum_favour = [0]*504
sum_tweets = [0]*504

#i=0
while len(line)!=0:
    tweet = json.loads(line)
    current_date = tweet['firstpost_date']
    #tweet_datetime = datetime.datetime.fromtimestamp(tweet['firstpost_date'])	
    if current_date>=nhmin and current_date < nhmax:
        ihour = (tweet['firstpost_date']-nhmin)/3600
        ntweets_hour[ihour] += 1
        
    if current_date>=mintime and current_date < maxtime:
        ihour = (tweet['firstpost_date']-mintime)/3600
        time_of_day[ihour] = (datetime.datetime.fromtimestamp(current_date)).hour
        #i += 1
        sum_tweets[ihour] += 1
    
    
    # number of followers of the current user posting the tweet
        nfollowers = int(tweet['tweet']['user']['followers_count'])
        sum_followers[ihour] += nfollowers
        if nfollowers>max_followers[ihour]:
            max_followers[ihour] = nfollowers
        #sum_users += 1.0				
				
				# number of retweets
        n_retweets = tweet['metrics']['citations']['total']
        sum_retweets[ihour] += n_retweets
        
        rs = tweet['metrics']['ranking_score']
        ranking_score[ihour] += rs
        
        num_friend = tweet['tweet']['user']['friends_count']
        sum_friends[ihour] += num_friend
        
        n_favour = tweet['tweet']['user']['favourites_count']
        sum_favour[ihour] += n_favour
        

    line = f.readline()

Y = ntweets_hour    
X = np.mat([sum_followers, max_followers, sum_retweets, time_of_day, ranking_score, sum_friends, sum_favour, sum_tweets])
X = X.transpose()
X = sm.add_constant(X, prepend=False)

model = sm.OLS(Y, X)
result = model.fit()
print result.summary()
Y_predict = abs(result.predict(X))
err =np.mean(abs((Y_predict.transpose())-(np.array(Y)).transpose()))
per = err/np.mean((np.array(Y)).transpose())
print per

plt.scatter(sum_followers,ntweets_hour,marker = '.')
plt.xlim(0,max(sum_followers))
plt.ylim(0,max(ntweets_hour))
fig = plt.gcf()
fig.set_size_inches(10,8)
fig.savefig('p3 ' + string + ' sum of followers', dpi=100)
plt.show()
plt.scatter(sum_retweets,ntweets_hour,marker = '.')
plt.xlim(0,max(sum_retweets))
plt.ylim(0,max(ntweets_hour))
fig = plt.gcf()
fig.set_size_inches(10,8)
fig.savefig('p3 ' + string + ' sum of retweets', dpi=100)
plt.show()
plt.scatter(sum_favour,ntweets_hour,marker = '.')
plt.xlim(0,max(sum_favour))
plt.ylim(0,max(ntweets_hour))
fig = plt.gcf()
fig.set_size_inches(10,8)
fig.savefig('p3 ' + string + ' sum of favourites', dpi=100)
plt.show()
plt.scatter(max_followers,ntweets_hour,marker = '.', color = 'c')
plt.xlim(0,max(max_followers))
plt.ylim(0,max(ntweets_hour))
fig = plt.gcf()
fig.set_size_inches(10,8)
fig.savefig('p3 ' + string + ' max followers', dpi=100)
plt.show()
plt.scatter(sum_tweets,ntweets_hour,marker = '.', color = 'r')
plt.xlim(0,max(sum_tweets))
plt.ylim(0,max(ntweets_hour))
fig = plt.gcf()
fig.set_size_inches(10,8)
fig.savefig('p3 ' + string + ' sum of current hour tweets', dpi=100)
plt.show()
plt.scatter(ranking_score, ntweets_hour, marker = '.', color = 'g')
plt.xlim(0,max(ranking_score))
plt.ylim(0,max(ntweets_hour))
fig = plt.gcf()
fig.set_size_inches(10,8)
fig.savefig('p3 ' + string + ' sum of ranking score', dpi=100)
plt.show()
plt.scatter(sum_friends, ntweets_hour, marker = '.', color = 'k')
plt.xlim(0,max(sum_friends))
plt.ylim(0,max(ntweets_hour))
fig = plt.gcf()
fig.set_size_inches(10,8)
fig.savefig('p3 ' + string + ' sum of friends', dpi=100)
plt.show()