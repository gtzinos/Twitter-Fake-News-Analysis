from config.database import *
from config.credentials import *
from database.connect import openConnection
from database.users import Users
from database.tweets import Tweets

from twitter.login import *
from user.info import *
from twitter.owner import *

from user.friendship import readDataFromJSON

#Open connection
db = openConnection(db_hostname, db_name, db_port)

#Login user
auth_api = login(consumer_key, consumer_secret, access_token, access_token_secret)
#Owner login
loggedInUser = getUser(username, auth_api)
# Calculate the average number of tweets per day
printUserDetails(loggedInUser)

#Insert user
userModel = Users(users_table_name)
userModel.insert_if_not_exists(db, loggedInUser)

#Get all tweets from database
allUserTweets = Tweets(tweets_table_name).find_all_by_owner_id(db, loggedInUser.id)


#Get Tweets from owner
getTweets(loggedInUser, auth_api)

# Url from a single tweet by WSJ
# https://twitter.com/i/web/status/984269901333450753 <-- TWEET ID


# print("--------------------------------------")

# tweetIdListHuzler = getTweets(HuzlersUser, auth_api)
# print("-------------------------")
# pprint.pprint(tweetIdListHuzler[0])
# print("-------------------------")
# retweetsHuzler = getRetweets(tweetIdListHuzler[1],auth_api)
# retweetsHuzler = getRetweeters(tweetIdListHuzler[1],auth_api)

# 
# print(retweetsHuzler)


# Run it only one time!
# insertData()

# showData()

# checkFriendship(2302467404,'BrianZ_CR')
readDataFromJSON('h_1.json')
