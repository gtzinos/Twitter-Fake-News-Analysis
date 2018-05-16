from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import json

import sys

hashtags = []
mentions = []
end_date = datetime.utcnow() - timedelta(days=30)
def getHashtagsUsers(auth_api,user_tweets):
    tweet_count = 0

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
        print
        print("Most mentioned Twitter users:")
        for item, count in Counter(mentions).most_common(10):
            print(item + "\t" + str(count))
        print
        print("Most used hashtags:")
        for item, count in Counter(hashtags).most_common(10):
            print(item + "\t" + str(count))

        print
        print("All done. Processed " + str(tweet_count) + " tweets.")
        print

def getStatus(auth_api):
    for tweet in Cursor(auth_api.user_timeline).items():
        process_or_store(tweet._json)

def process_or_store(tweet):
        print(json.dumps(tweet))