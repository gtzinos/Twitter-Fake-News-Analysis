import tweepy
#from tweepy import *
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
from config import *

from user.login import *
from user.WSJTweets import *
from user.HuzlerTweets import *
from user.info import *
from user.hashtagsAndUsers import *
from tweepy import parsers

from database.transactions import insertData, showData
from user.friendship import checkFriendship, readDataFromJSON
import pprint as pp

#auth_api = login(consumer_key, consumer_secret, access_token, access_token_secret)

# WSJ_tweets = 'WSJ'
Huzlers_tweets = 'TheHuzlers'

# WSJUser = getUser(WSJ_tweets, auth_api)
#HuzlersUser = getUser(Huzlers_tweets,auth_api)
# Calculate the average number of tweets per day
# printUserDetails(WSJUser)
#print("------------------------------")
# printUserDetails(HuzlersUser)

# Url from a single tweet by WSJ
# https://twitter.com/i/web/status/984269901333450753 <-- TWEET ID


#get most mentioned hashtags and users
# getHashtagsUsers(auth_api,user_tweets)
#print("----------------------------")
# getStatus(auth_api)

#Get Tweets

# stuff = auth_api.user_timeline(screen_name = loggedUser.screen_name, count = 100, include_rts = True)
# print('More info:')
# print(stuff)

# print("------------RETWEET INFO WSJ-------------")
# getTweetsWSJ(WSJUser, auth_api)
#print("------------RETWEET INFO TheHuzlers-------------")
#getTweetsHuzlers(HuzlersUser,auth_api)

#print("------------THE END-------------")
#tweetIdListWSJ = getTweets(WSJUser, auth_api)
#print("-------------------------")
#pprint.pprint(tweetIdListWSJ[0])
#print("-------------------------")


#print("--------------------------------------")

# tweetIdListHuzler = getTweets(HuzlersUser, auth_api)
# print("-------------------------")
# pprint.pprint(tweetIdListHuzler[0])
# print("-------------------------")
# retweetsHuzler = getRetweets(tweetIdListHuzler[1],auth_api)
# retweetsHuzler = getRetweeters(tweetIdListHuzler[1],auth_api)

# 
# print(retweetsHuzler)


#Run it only one time!
#insertData()

#showData()

#checkFriendship(2302467404,'BrianZ_CR')
readDataFromJSON('h_1.json')