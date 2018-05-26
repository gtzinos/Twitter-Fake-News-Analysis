import tweepy
from tweepy import *
import csv
import json
import pprint
import re
from collections import OrderedDict

from config.database import tweets_table_name, retweets_table_name, followers_table_name
from database.followers import Followers
from database.retweets import Retweets
from database.tweets import Tweets


def getTweets(loggedInUser, auth_api, db):
    tweetsModel = Tweets(tweets_table_name)

    tweets = tweepy.Cursor(auth_api.user_timeline, screen_name=loggedInUser.screen_name, include_rts=True)

    # Get all tweets
    for tweet in tweets.items():
        tweetsModel.insert_if_not_exists(db, tweet.id, tweet._json)


def getRetweetsOfTop3(loggedInUser, auth_api, db):
    tweetsModel = Tweets(tweets_table_name)
    retweetsModel = Retweets(retweets_table_name)

    top3Tweets = tweetsModel.find_top_3(db, loggedInUser.id)

    for tweet in top3Tweets:
        try:
            page = 0

            while True:
                retweets = auth_api.retweets(tweet['id'], page=page, count=100)

                if len(retweets) > 0:
                    for retweet in retweets:
                        retweetsModel.insert_if_not_exists(db, retweet.id, retweet._json)

                    page += 1
                else:
                    break
        except Exception as e:
            print(e)

    print("Done")


def getFollowers(loggedInUser, auth_api, db):
    retweetsModel = Retweets(retweets_table_name)
    followersModel = Followers(followers_table_name)
    hop_number = 1

    # Check all retweeters with owner page

    # get all not in followers collection
    available_retweeters = retweetsModel.find_all_not_in_followers(db, followers_table_name, loggedInUser.id)

    for available_retweeter in available_retweeters:
        isFollower = auth_api.show_friendship(source_id=available_retweeter['user']['id'],
                                              target_id=loggedInUser.id)[0].followed_by
        if isFollower:
            followersModel.insert_if_not_exists(db, {
                "source": available_retweeter,
                "target": {'user': {'id': loggedInUser.id}},
                "hop_number": hop_number
            })

    # Check all available with last insert
    found_followers = 1

    while found_followers > 0:
        hop_number += 1
        # clear value
        found_followers = 0
        # get all not in followers collection
        available_retweeters = retweetsModel.find_all_not_in_followers(db, followers_table_name, loggedInUser.id)
        last_inserted_followers = followersModel.get_last_inserted_hop(db, loggedInUser.id)

        for available_retweeter in available_retweeters:
            for last_inserted_follower in last_inserted_followers:

                isFollower = api.show_friendship(source_id=available_retweeter['id'],
                                                 target_screen_name=last_inserted_follower['id']).followedBy
                if isFollower:
                    followersModel.insert_if_not_exists(db, {
                        "source": available_retweeter,
                        "target": {'user': {'id': last_inserted_follower}},
                        "hop_number": hop_number
                    })
                    found_followers += 1
