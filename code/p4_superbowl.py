# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 22:18:50 2016

@author: Qiyue
"""

#problem 4

import numpy as np
import statsmodels.api as sm
import json
import datetime, time
#import matplotlib.pyplot as plt
import sklearn
from sklearn.cross_validation import KFold
import pickle as pickle

def HL(hour):
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
    

f = open('tweet_data/tweets_#superbowl.txt')

line = f.readline()

#import json
tweet = json.loads(line)

tweet['tweet']['text']
start_date = datetime.datetime(2015,1,18, 0,0,0)
date1 = datetime.datetime(2015,2,1, 8,0,0)
date2 = datetime.datetime(2015,2,1, 20,0,0)
end_date = datetime.datetime(2015,2,8, 0,0,0)
nhsd = datetime.datetime(2015,1,18, 1,0,0)
nhdate1 = datetime.datetime(2015,2,1, 9,0,0)
nhdate2 = datetime.datetime(2015,2,1, 21,0,0)
nhed = datetime.datetime(2015,2,8, 1,0,0)

mintime = int(time.mktime(start_date.timetuple()))
period1 = int(time.mktime(date1.timetuple()))
period2 = int(time.mktime(date2.timetuple()))
maxtime = int(time.mktime(end_date.timetuple()))

nht1 = int(time.mktime(nhsd.timetuple()))
nht2 = int(time.mktime(nhdate1.timetuple()))
nht3 = int(time.mktime(nhdate2.timetuple()))
nht4 = int(time.mktime(nhed.timetuple()))

#period 1 2 weeks before superbowl til 8am 2/1
print "Getting data"
print "============================================================="
ntweets_hour = [0]*344
sum_followers = [0]*344
max_followers = [0]*344
sum_retweets = [0]*344
time_of_day = [0]*344
ranking_score = [0.]*344
sum_friends = [0.]*344
sum_favour = [0]*344
sum_tweets = [0]*344

ntweets_hour2 = [0]*12
sum_followers2 = [0]*12
max_followers2 = [0]*12
sum_retweets2 = [0]*12
time_of_day2 = [0]*12
ranking_score2 = [0.]*12
sum_friends2 = [0.]*12
sum_favour2 = [0]*12
sum_tweets2 = [0]*12
hot_level = [0]*12

ntweets_hour3 = [0]*148
sum_followers3 = [0]*148
max_followers3 = [0]*148
sum_retweets3 = [0]*148
time_of_day3 = [0]*148
ranking_score3 = [0.]*148
sum_friends3 = [0.]*148
sum_favour3 = [0]*148
sum_tweets3 = [0]*148


while len(line)!=0:
    tweet = json.loads(line)
    current_date = tweet['firstpost_date']

    if current_date>=nht1 and current_date < nht2:
        ihour = (tweet['firstpost_date']-nht1)/3600
        ntweets_hour[ihour] += 1
           
    if current_date>=mintime and current_date < period1:
        ihour = (tweet['firstpost_date']-mintime)/3600
        time_of_day[ihour] = (datetime.datetime.fromtimestamp(current_date)).hour
        
        sum_tweets[ihour]+=1;

        nfollowers = int(tweet['tweet']['user']['followers_count'])
        sum_followers[ihour] += nfollowers
        if nfollowers>max_followers[ihour]:
            max_followers[ihour] = nfollowers

        n_retweets = tweet['metrics']['citations']['total']
        sum_retweets[ihour] += n_retweets
        
        rs = tweet['metrics']['ranking_score']
        ranking_score[ihour] += rs
        
        num_friend = tweet['tweet']['user']['friends_count']
        sum_friends[ihour] += num_friend
        
        n_favour = tweet['tweet']['user']['favourites_count']
        sum_favour[ihour] += n_favour

#period 2
    if current_date>=nht2 and current_date < nht3:
        ihour = (tweet['firstpost_date']-nht2)/3600
        ntweets_hour2[ihour] += 1

    if current_date >= period1 and current_date < period2:
        ihour = (tweet['firstpost_date']-period1)/3600
        time_of_day2[ihour] = (datetime.datetime.fromtimestamp(current_date)).hour
        
        sum_tweets2[ihour]+=1;
    
        nfollowers = int(tweet['tweet']['user']['followers_count'])
        sum_followers2[ihour] += nfollowers
        if nfollowers>max_followers[ihour]:
            max_followers2[ihour] = nfollowers

        n_retweets = tweet['metrics']['citations']['total']
        sum_retweets2[ihour] += n_retweets
        
        rs = tweet['metrics']['ranking_score']
        ranking_score2[ihour] += rs
        
        num_friend = tweet['tweet']['user']['friends_count']
        sum_friends2[ihour] += num_friend
        
        n_favour = tweet['tweet']['user']['favourites_count']
        sum_favour2[ihour] += n_favour

        hot_level[ihour] = HL(ihour)


#period 3
    if current_date>=nht3 and current_date < nht4:
        ihour = (tweet['firstpost_date']-nht3)/3600
        ntweets_hour3[ihour] += 1

    if current_date >= period2 and current_date < maxtime:
        ihour = (tweet['firstpost_date']-period2)/3600
        time_of_day3[ihour] = (datetime.datetime.fromtimestamp(current_date)).hour

        sum_tweets3[ihour]+=1;
    
        nfollowers = int(tweet['tweet']['user']['followers_count'])
        sum_followers3[ihour] += nfollowers
        if nfollowers>max_followers[ihour]:
            max_followers3[ihour] = nfollowers

        n_retweets = tweet['metrics']['citations']['total']
        sum_retweets3[ihour] += n_retweets
        
        rs = tweet['metrics']['ranking_score']
        ranking_score3[ihour] += rs
        
        num_friend = tweet['tweet']['user']['friends_count']
        sum_friends3[ihour] += num_friend
        
        n_favour = tweet['tweet']['user']['favourites_count']
        sum_favour3[ihour] += n_favour        

    line = f.readline()

print "fitting and predicting"
print "============================================================="
print "period 1"
print "============================================================="
X = np.mat([sum_followers, sum_retweets, ranking_score, sum_friends, sum_favour, sum_tweets])
X = X.transpose()

y = np.array([ntweets_hour])
y = y.transpose()
kf = sklearn.cross_validation.KFold(344,n_folds=10,shuffle = True)

err_t = [0.]*10
i = 0
for train_index, test_index in kf:
    #print ("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    X_train = sm.add_constant(X_train, prepend=False)
    X_test = sm.add_constant(X_test, prepend=False)

    model = sm.OLS(y_train, X_train)
    result = model.fit()
    print result.summary()
    y_predict = abs(result.predict(X_test))
    err = np.mean(abs(y_predict.transpose()-y_test.transpose()))
    err_t[i] = err
    i +=1
    print "average error of test ", i, ": ", err

err_ave = np.mean(err_t)
print "average error of 10 tests: ", err_ave
print "============================================================="
print "period 2"
print "============================================================="
#sum_followers2, max_followers2, sum_retweets2, time_of_day2, ranking_score2, sum_friends2, sum_favour2
X2 = np.mat([sum_followers2,  ranking_score2, sum_friends2,sum_tweets2, hot_level])
X2 = X2.transpose()
y2 = np.array([ntweets_hour2])
y2 = y2.transpose()
X2 = sm.add_constant(X2, prepend=False)

kf2 = sklearn.cross_validation.KFold(12,n_folds=10,shuffle = True)

err_t = [0.]*10
i = 0
for train_index, test_index in kf2:
    #print ("TRAIN:", train_index, "TEST:", test_index)
    X2_train, X2_test = X2[train_index], X2[test_index]
    y2_train, y2_test = y2[train_index], y2[test_index]
#    X_train = sm.add_constant(X_train, prepend=False)
#    X_test = sm.add_constant(X_test, prepend=False)

    model = sm.OLS(y2_train, X2_train)
    result = model.fit()
    print result.summary()
    y2_predict = abs(result.predict(X2_test))
    err = np.mean(abs(y2_predict.transpose()-y2_test.transpose()))
    err_t[i] = err
    i +=1
    print "average error of test ", i, ": ", err

err_ave = np.mean(err_t)
print "average error of 10 tests: ", err_ave
print "============================================================="
print "period 3"
print "============================================================="
#sum_followers3, max_followers3, sum_retweets3, time_of_day3, ranking_score3, sum_friends3, sum_favour3
X3 = np.mat([sum_followers3, sum_retweets3,ranking_score3, sum_friends3, sum_favour3, sum_tweets3])
X3 = X3.transpose()

y3 = np.array([ntweets_hour3])
y3 = y3.transpose()
kf3 = sklearn.cross_validation.KFold(148,n_folds=10,shuffle = True)

err_t = [0.]*10
i = 0
for train_index, test_index in kf3:
    #print ("TRAIN:", train_index, "TEST:", test_index)
    X3_train, X3_test = X3[train_index], X3[test_index]
    y3_train, y3_test = y3[train_index], y3[test_index]
    X3_train = sm.add_constant(X3_train, prepend=False)
    X3_test = sm.add_constant(X3_test, prepend=False)

    model = sm.OLS(y3_train, X3_train)
    result = model.fit()
    s = pickle.dumps(model)
    print result.summary()
    y3_predict = abs(result.predict(X3_test))
    err = np.mean(abs(y3_predict.transpose()-y3_test.transpose()))
    err_t[i] = err
    i +=1
    print "average error of test ", i, ": ", err

err_ave = np.mean(err_t)
print "average error of 10 tests: ", err_ave
print "============================================================="
