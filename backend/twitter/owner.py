# -*- coding: utf-8 -*-
import tweepy
from tweepy import *

from config.database import *
from database.connect import openConnection
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


def get_retweeters_memory(available_retweeters_cursor):
    available_retweeters_memory = []

    for available_retweeter in available_retweeters_cursor:
        available_retweeters_memory.append({
            'user': available_retweeter['user'],
            '_id': available_retweeter['_id']
        })

    return available_retweeters_memory


def get_last_inserted_memory(last_inserted_cursor):
    last_inserted_memory = []

    for last_inserted in last_inserted_cursor:
        last_inserted_memory.append({
            'source': last_inserted['source'],
            'target': last_inserted['target']
        })

    return last_inserted_memory


def are_followers(auth_api, sourceUserId, targetUserId):
    try:
        print("Source: " + str(sourceUserId) + " Target: " + str(targetUserId))

        are_followers_results = auth_api.show_friendship(source_id=sourceUserId,
                                                        target_id=targetUserId)

        final_decision = are_followers_results[0].followed_by or are_followers_results[0].following

        print(final_decision)

        return final_decision
    except Exception as e:
        print("touipai final decision")
        print(e)
        return False



def getFollowers(loggedInUserTweepy, auth_api):
    db = openConnection(db_hostname, db_name, db_port, db_username, db_password, db_authMechanism)
    loggedInUser = loggedInUserTweepy._json

    retweetsModel = Retweets(retweets_table_name)
    followersModel = Followers(followers_table_name)
    hop_number = 1

    # Check all retweeters with owner page

    # get all not in followers collection
    available_retweeters = retweetsModel.find_all_mine(db, loggedInUser['id'])

    available_retweeters_memory = get_retweeters_memory(available_retweeters)

    print("Step 1 Followers")

    for available_retweeter_memory in available_retweeters_memory:
        are_followers_result = are_followers(auth_api, available_retweeter_memory['user']['id'], loggedInUser['id'])

        if are_followers_result:

            followersModel.insert_if_not_exists(db, {
                "source": available_retweeter_memory,
                "target": {'user': loggedInUser},
                "from_owner": loggedInUser,
                "hop_number": hop_number
            })

    # Check all available with last insert
    found_followers = 1

    print("Step 2 Followers")

    try:
        while found_followers > 0:
            print(hop_number)
            hop_number += 1

            print("hop: " + str(hop_number))

            # clear value
            found_followers = 0
            # get all not in followers collection

            available_retweeters = retweetsModel.find_all_not_in_followers(db, followers_table_name, loggedInUser['id'])
            available_retweeters_memory = get_retweeters_memory(available_retweeters)

            last_inserted_followers = followersModel.get_last_inserted_hop(db, loggedInUser['id'])
            last_inserted_followers_memory = get_last_inserted_memory(last_inserted_followers)

            for available_retweeter_memory in available_retweeters_memory:
                for last_inserted_follower_memory in last_inserted_followers_memory:
                    who_to_compare = "source"
                    if available_retweeter_memory['user']['id'] == last_inserted_follower_memory['source']['user']['id']:
                        who_to_compare = "target"

                    are_followers_result = are_followers(auth_api, available_retweeter_memory['user']['id'],
                                                        last_inserted_follower_memory[who_to_compare]['user']['id'])
                    if are_followers_result:
                        followersModel.insert_if_not_exists(db, {
                            "source": available_retweeter_memory,
                            "target": last_inserted_follower_memory[who_to_compare],
                            "from_owner": loggedInUser,
                            "hop_number": hop_number
                        })
                        found_followers += 1
    except Exception as e:
        print("ERROR!")
        print(e)
