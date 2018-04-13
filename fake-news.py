
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
from config import *
from user import *

auth_api = login(consumer_key, consumer_secret, access_token, access_token_secret)

loggedUser = getUser(user_tweets, auth_api)

#stuff = auth_api.user_timeline(screen_name = loggedUser.screen_name, count = 100, include_rts = True)
#print('More info:')
# print(stuff)

# Calculate the average number of tweets per day

tweets = loggedUser.statuses_count
account_created_date = loggedUser.created_at
delta = datetime.utcnow() - account_created_date
account_age_days = delta.days
print("Account age (in days): " + str(account_age_days))

print("Account age (in years): " + str(account_age_days/365))

if account_age_days > 0:
    print("Average tweets per day: " + "%.2f" %
          (float(tweets)/float(account_age_days)))

# Url from a single tweet by WSJ
# https://twitter.com/i/web/status/984269901333450753 <-- TWEET ID


# Not working
hashtags = []
mentions = []
tweet_count = 0
end_date = datetime.utcnow() - timedelta(days=30)
for status in Cursor(auth_api.user_timeline, id=user_tweets).items():
    tweet_count += 1
    if hasattr(status, "entities"):
        entities = status.entities
        if "hashtags" in entities:
            for ent in entities["hashtags"]:
                if ent is not None:
                    if "text" in ent:
                        hashtag = ent["text"]
                        if hashtag is not None:
                            hashtags.append(hashtag)
        if "user_mentions" in entities:
            for ent in entities["user_mentions"]:
                if ent is not None:
                    if "screen_name" in ent:
                        name = ent["screen_name"]
                        if name is not None:
                            mentions.append(name)
    if status.created_at < end_date:
        break
