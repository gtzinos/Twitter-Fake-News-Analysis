from tweepy import *
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
from config import access_token, access_token_secret, consumer_key, consumer_secret, Huzlers_tweets, WSJ_tweets


from user.login import login, getUser
from user.tweets import getTweets, filterText, PrintMembers
from user.info import printUserDetails
from user.hashtagsAndUsers import getHashtagsUsers, getStatus, process_or_store
from tweepy import parsers

auth_api = login(consumer_key, consumer_secret, access_token, access_token_secret)

WSJUser = getUser(WSJ_tweets, auth_api)
HuzlersUser = getUser(Huzlers_tweets,auth_api)
# Calculate the average number of tweets per day
printUserDetails(WSJUser)
print("------------------------------")
printUserDetails(HuzlersUser)

# Url from a single tweet by WSJ
# https://twitter.com/i/web/status/984269901333450753 <-- TWEET ID


#get most mentioned hashtags and users
# getHashtagsUsers(auth_api,user_tweets)
print("----------------------------")
# getStatus(auth_api)

#Get Tweets

# stuff = auth_api.user_timeline(screen_name = loggedUser.screen_name, count = 100, include_rts = True)
# print('More info:')
# print(stuff)

print("------------RETWEET INFO WSJ-------------")
getTweets(WSJUser, auth_api)
print("------------RETWEET INFO TheHuzlers-------------")
getTweets(HuzlersUser,auth_api)

print("------------THE END-------------")
#tweetIdListWSJ = getTweets(WSJUser, auth_api)
print("-------------------------")
#pprint.pprint(tweetIdListWSJ[0])
print("-------------------------")


print("--------------------------------------")

# tweetIdListHuzler = getTweets(HuzlersUser, auth_api)
# print("-------------------------")
# pprint.pprint(tweetIdListHuzler[0])
# print("-------------------------")
# retweetsHuzler = getRetweets(tweetIdListHuzler[1],auth_api)
# retweetsHuzler = getRetweeters(tweetIdListHuzler[1],auth_api)

# 
# print(retweetsHuzler)
