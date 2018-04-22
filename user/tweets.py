import csv
import tweepy
from tweepy import *
import json


FILE_WSJ = 'WSJ.json'


def getTweets (loggedUser,auth_api):
    with open(FILE_WSJ,'w') as f_out:
        for tweet in tweepy.Cursor(auth_api.user_timeline, screen_name = loggedUser.screen_name, include_rts = True).items():
            # json.dump(tweet._json, f_out)
            # f_out.write('\n')
            print("Tweet Text: ", tweet.text ,"retweeted #:" , tweet.retweet_count)
            print('\n')
    print("Finished...")

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
