from tweepy import OAuthHandler
from tweepy import API

def getUser(user_tweets, auth_api):

	print('Getting data for user: '+ user_tweets)

	loggedUser = auth_api.get_user(user_tweets)

	print("name: " + loggedUser.name)
	print("screen_name: " + loggedUser.screen_name)
	print("description: " + loggedUser.description)
	print("statuses_count: " + str(loggedUser.statuses_count))
	print("friends_count: " + str(loggedUser.friends_count))
	print("followers_count: " + str(loggedUser.followers_count))

	return loggedUser

def login(consumer_key, consumer_secret, access_token, access_token_secret):
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return API(auth,retry_count=5,
                 retry_delay=10,
                 retry_errors=set([401, 404, 500, 503]),
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
