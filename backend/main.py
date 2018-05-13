from tweepy import *
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
from config import *
from user import *
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

tweetIdListWSJ = getTweets(WSJUser, auth_api)
print("-------------------------")
pprint.pprint(tweetIdListWSJ[0])
print("-------------------------")
retweetsWSJ = getRetweeters(tweetIdListWSJ[0],auth_api)
print("------------RETWEET INFO WSJ-------------")
print(retweetsWSJ)
# getTweetsByQuery(auth_api, "Tsipras", "en")
# getTweets2(auth_api)
print("--------------------------------------")

tweetIdListHuzler = getTweets(HuzlersUser, auth_api)
print("-------------------------")
pprint.pprint(tweetIdListHuzler[0])
print("-------------------------")
retweetsHuzler = getRetweeters(tweetIdListHuzler[0],auth_api)
print("------------RETWEET INFO TheHuzlers-------------")
print(retweetsHuzler)
