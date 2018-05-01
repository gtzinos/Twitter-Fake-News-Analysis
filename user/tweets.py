import csv
import tweepy
from tweepy import *
import json
import pprint
from collections import OrderedDict


FILE_WSJ = 'WSJ.json'

def getTweets (loggedUser,auth_api):
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
    return tweetIdList[-3:]
    # for k, v in sortedTweetDict.items():
    #     print k, v

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
    # results = auth_api.retweets(id=tweetId, count=100)
    # return results
    p=1
    while True:
        results = auth_api.retweets(id=tweetId, page= p, count=100)
        if results:
            print(results['author'])
            p=p+1
        else:
            break

def getRetweeters(tweetId,auth_api):
    results = auth_api.retweeters(id=tweetId)
    return results
