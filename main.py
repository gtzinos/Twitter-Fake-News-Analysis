from tweepy import *
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
from config import *
from user import *
from tweepy import parsers

auth_api = login(consumer_key, consumer_secret, access_token, access_token_secret)

loggedUser = getUser(user_tweets, auth_api)

# Calculate the average number of tweets per day
printUserDetails(loggedUser)


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

tweetIdList = getTweets(loggedUser, auth_api)
print("-------------------------")
pprint.pprint(tweetIdList[0])
print("-------------------------")
retweets = getRetweeters(tweetIdList[0],auth_api)
print("------------RETWEET INFO-------------")
print(retweets)
# getTweetsByQuery(auth_api, "Tsipras", "en")
# getTweets2(auth_api)
