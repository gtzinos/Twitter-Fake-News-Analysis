# -*- coding: utf-8 -*-
from tweepy import OAuthHandler
from tweepy import API


def getUser(user_tweets, auth_api):
    print('Getting data for user: ' + user_tweets)

    logged_user = auth_api.get_user(user_tweets)

    print("name: " + logged_user.name)
    print("screen_name: " + logged_user.screen_name)
    print("description: " + logged_user.description)
    print("statuses_count: " + str(logged_user.statuses_count))
    print("-------------------------------------")
    print("friends_count: " + str(logged_user.friends_count))
    print("-------------------------------------")
    print("followers_count: " + str(logged_user.followers_count))
    print("-------------------------------------")

    return logged_user


def login(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return API(auth, retry_count=5,
               retry_delay=10,
               retry_errors=set([401, 404, 500, 503]),
               wait_on_rate_limit=True,
               wait_on_rate_limit_notify=True)
