from database.connect import openConnection
from database.users import Users
from twitter.login import *
from twitter.owner import *
from config.database import *
from config.credentials import *

# Open connection
from user.info import printUserDetails

db = openConnection(db_hostname, db_name, db_port, db_username, db_password, db_authMechanism)

# Login user
auth_api = login(consumer_key, consumer_secret, access_token, access_token_secret)
# Owner login
loggedInUser = getUser(username, auth_api)
# Calculate the average number of tweets per day
printUserDetails(loggedInUser)

# Insert user
userModel = Users(users_table_name)
userModel.insert_if_not_exists(db, loggedInUser.id, loggedInUser._json)

# Get all tweets from database
#allUserTweets = Tweets(tweets_table_name).find_all_by_owner_id(db, loggedInUser.id)

# Get Tweets from owner
getTweets(loggedInUser, auth_api, db)

# Get Retweets for top 3 Tweets
getRetweetsOfTop3(loggedInUser, auth_api, db)

# Get follower of retweets of 3 top tweets
getFollowers(loggedInUser, auth_api, db)

# Get followers for Retweets of top 3 Tweets