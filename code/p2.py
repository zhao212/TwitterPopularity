# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 22:18:50 2016

@author: Qiyue
"""

#problem 2

import numpy as np
import statsmodels.api as sm
import json
import datetime, time
from sklearn.linear_model import LinearRegression

f = open('tweet_data/tweets_#superbowl.txt')

line = f.readline()

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
ntweets_hour = [0]*504 
sum_followers = [0]*504
max_followers = [0]*504
sum_retweets = [0]*504
#sum_tweets = 0.
time_of_day = [0]*504
sum_tweets = [0]*504

#i=0
while len(line)!=0:
    tweet = json.loads(line)
    current_date = tweet['firstpost_date']
    if current_date>=nhmin and current_date < nhmax:
        ihour = (tweet['firstpost_date']-nhmin)/3600
        ntweets_hour[ihour] += 1
        
    if current_date>=mintime and current_date < maxtime:
        ihour = (tweet['firstpost_date']-mintime)/3600
        time_of_day[ihour] = (datetime.datetime.fromtimestamp(current_date)).hour

        sum_tweets[ihour] += 1
        nfollowers = int(tweet['tweet']['user']['followers_count'])
        sum_followers[ihour] += nfollowers
        if nfollowers>max_followers[ihour]:
            max_followers[ihour] = nfollowers

        n_retweets = tweet['metrics']['citations']['total']
        sum_retweets[ihour] += n_retweets

    line = f.readline()

Y = ntweets_hour    
X = np.mat([sum_followers, max_followers, sum_retweets, time_of_day, sum_tweets])
X = X.transpose()
X = sm.add_constant(X, prepend=False)

model = sm.OLS(Y, X)
result = model.fit()
Y_predict = result.predict(X)
err =np.mean(abs((Y_predict.transpose())-(np.array(Y)).transpose()))
per = err/np.mean((np.array(Y)).transpose())
print per
print result.summary()
