from user import *
from user import login
from config import *
import collections

auth_api=login(consumer_key,consumer_secret,access_token,access_token_secret)

if auth_api:
    print("Login success!")
else:
    print("Can't login!")

userWSJ=getUser(WSJ_tweets,auth_api)
#userTH=getUser(Huzlers_tweets,auth_api)

#WSJ id
idWsj=userWSJ.id
#WSJ json
jsonWsj=userWSJ._json
#WSJ statuses_count
statusesCount=userWSJ.statuses_count

#tweets=getTweets(userWSJ,auth_api)

tweetsWSJ = auth_api.user_timeline(screen_name =userWSJ.screen_name, count=100, include_rts=True)
tweets=list()

class CustomTweet:
    id_str=""
    retweet_num=0

for status in tweetsWSJ:
    #print("Tweet id: ",status.id_str)
    print("Tweet retweet_count: ",status.retweet_count)
    #print("Tweet text: ",status.text)
    x=CustomTweet()
    x.id_str=status.id_str
    x.retweet_num=status.retweet_count

    tweets.append(x)

print("Unordered list:")
print(" ")
for item in tweets:
    print(item.id_str,item.retweet_num)

tweets.sort(key=lambda x: x.retweet_num, reverse=True)
newList=sorted(tweets, key=lambda x: x.retweet_num, reverse=True)

print("Ordered list:")
print(" ")
for i in newList:
    print(i.id_str,i.retweet_num)

print("")
print("Top 3 tweet ids with most retweets: ")
print(newList[0].id_str,newList[0].retweet_num)
print(newList[1].id_str,newList[1].retweet_num)
print(newList[2].id_str,newList[2].retweet_num)