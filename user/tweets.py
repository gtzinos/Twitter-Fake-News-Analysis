import csv
import tweepy
from tweepy import *
import json
import pprint
from collections import OrderedDict

#This is for testing only
"""def getTweets (loggedUser,auth_api):
    
    retweeterCounter = 1
    counter = 0
    p=0
    tweetDict = {}
    tweetList = list()
    for tweet in tweepy.Cursor(auth_api.user_timeline, screen_name = loggedUser.screen_name, include_rts = True).items():
        tweetDict.update({tweet.id:tweet.retweet_count})
        counter += 1
        
    print("Finished... with count: ",counter)
    sortedTweetDict = OrderedDict(sorted(tweetDict.items(), key=lambda x:x[1]))
    tweetRetweetNoList = list(sortedTweetDict.values())
    print("How many retweets with top 3: " + str(tweetRetweetNoList[-3:]))
    tweetIdList = list(sortedTweetDict.keys())
    print("The top 3 tweets with ID: " + str(tweetIdList[-3:]))
    topThree = tweetIdList[-3:]
    for tweetId in topThree:
        print("---------------------------------------")
        print("Printing retweeters for tweet: " + str(retweeterCounter) +":" +str(tweetId))
        for retweet in auth_api.retweets(tweetId,page=p):
            try:
                print("USER:", retweet.user.screen_name)
                tweetList.append(retweet.user.screen_name)
                p = p +1
            except tweepy.TweepError:
                print("waiting...")
                continue
        retweeterCounter += 1
    
    print("Retweeters found: "+str(p))
    return tweetList """
#This is production
def getTweets (loggedUser,auth_api):
    
    retweeterCounter = 0
    counter = 0
    p=0
    tweetDict = {}
    tweetList = list()
    for tweet in tweepy.Cursor(auth_api.user_timeline, screen_name = loggedUser.screen_name, include_rts = True).items():
        tweetDict.update({tweet.id:tweet.retweet_count})
        counter += 1
        
    print("Finished... with count: ",counter)
    sortedTweetDict = OrderedDict(sorted(tweetDict.items(), key=lambda x:x[1]))
    tweetRetweetNoList = list(sortedTweetDict.values())
    print("How many retweets with top 3: " + str(tweetRetweetNoList[-3:]))
    tweetIdList = list(sortedTweetDict.keys())
    print("The top 3 tweets with ID: " + str(tweetIdList[-3:]))
    topThree = tweetIdList[-3:]
    print("---------------------------------------")
    print("Printing retweeters for tweet: " +str(topThree[2]))
    while(True):
        retweets = auth_api.retweets(topThree[2],page=p)
        for retweet in retweets:
            if(retweet):
                try:
                    print("USER:", retweet.user.screen_name)
                    tweetList.append(retweet.user.screen_name)
                    retweeterCounter += 1
                except tweepy.TweepError:
                    print("waiting...")
                    continue
        p = p +1
    print("Retweeters found: "+str(retweeterCounter) + "in #" +str(p) +"pages")
    return tweetList

def getTweetsByQuery(auth_api, query,languageCode):
    for tweet in tweepy.Cursor(auth_api.search, q=query, lang=languageCode).items():
        print tweet

def getTweets2(auth_api):
    for tweet in tweepy.Cursor(auth_api.search,
                           q="WSJ",
                           rpp=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
        print tweet.text

"""def getRetweets(tweetId,auth_api):
    p=1
    while True:
        results = auth_api.retweets(id=tweetId, page= p)
        if results:
            print(results)  
            p=p+1
        else:
            break
    print (p)"""

"""def getRetweeters(tweetId,auth_api):
    results = auth_api.retweeters(id=tweetId)
    return results"""

def PrintMembers(obj):
    for attribute in dir(obj):
        
        #We don't want to show built in methods of the class
        if not attribute.startswith('__'):
            print(attribute)
