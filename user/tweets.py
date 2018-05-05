import csv
import tweepy
from tweepy import *
import json
import pprint
from collections import OrderedDict


FILE_WSJ = 'WSJ.json'
retweetCounter = 0
""" def getTweets (loggedUser,auth_api):
    counter = 0
    tweetDict = {}
    with open(FILE_WSJ,'w') as f_out:
        for tweet in tweepy.Cursor(auth_api.user_timeline, screen_name = loggedUser.screen_name, include_rts = True).items():
            # json.dump(tweet._json, f_out)
            # f_out.write('\n')
            # print("Tweet Text: ", tweet.text ,"retweeted #:" , tweet.retweet_count)
            # print('\n')
            tweetDict.update({tweet.id:tweet.retweet_count})
            counter += 1
    print("Finished... with count: ",counter)
    sortedTweetDict = OrderedDict(sorted(tweetDict.items(), key=lambda x:x[1]))
    tweetRetweetNoList = list(sortedTweetDict.values())
    print(tweetRetweetNoList[-3:])
    tweetIdList = list(sortedTweetDict.keys())
    print(tweetIdList[-3:])
    return tweetIdList[-3:] """
###TODO FIX 
def getTweets(loggedUser,auth_api):
    tweetList = list()
    p=1
    for tweet in auth_api.user_timeline(screen_name = loggedUser.screen_name):
        print("TWEET:", tweet.text)
        for reTweet in auth_api.retweets(tweet.id, count=100):
            print("USER:", reTweet.user.screen_name)
            tweetList.append(reTweet.user.screen_name)
            p = p +1
    print(p)
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

def getRetweets(tweetId,auth_api):
    p=1
    while True:
        results = auth_api.retweets(id=tweetId, page= p)
        if results:
            print(results)  
            p=p+1
        else:
            break
    print (p)

def getRetweeters(tweetId,auth_api):
    results = auth_api.retweeters(id=tweetId)
    return results

def PrintMembers(obj):
    for attribute in dir(obj):
        
        #We don't want to show built in methods of the class
        if not attribute.startswith('__'):
            print(attribute)
