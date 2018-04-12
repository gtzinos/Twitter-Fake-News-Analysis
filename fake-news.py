from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys

consumer_key = "PmOtnHDeLol5iTFJfT0SzhngX"
consumer_secret = "VPVLEZKDNg0pQn3FAoXepwUuR8cRM0vQ5B2xKJnZAvvDel67eD"
access_token = "296863841-ySiLADayokktc0JFtVGcQbd7afwbbVR9B4HxcfTi"
access_token_secret = "QU6QdwWhe1emH4qaWyaxw9gsR9iiUFc3jWa9cOCU5Jztu"


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

selected_user = 'WSJ'

print('Getting data for user: '+selected_user)

item = auth_api.get_user(selected_user)

print("name: " + item.name)
print("screen_name: " + item.screen_name)
print("description: " + item.description)
print("statuses_count: " + str(item.statuses_count))
print("friends_count: " + str(item.friends_count))
print("followers_count: " + str(item.followers_count))


#stuff = auth_api.user_timeline(screen_name = item.screen_name, count = 100, include_rts = True)
#print('More info:')
# print(stuff)

#Calculate the average number of tweets per day

tweets = item.statuses_count
account_created_date = item.created_at
delta = datetime.utcnow() - account_created_date
account_age_days = delta.days
print("Account age (in days): " + str(account_age_days))

print("Account age (in years): " + str(account_age_days/365))

if account_age_days > 0:
    print("Average tweets per day: " + "%.2f" %
          (float(tweets)/float(account_age_days)))
