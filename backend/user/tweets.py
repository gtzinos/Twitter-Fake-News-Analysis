import csv
import tweepy
from tweepy import *
import json
import pprint
from collections import OrderedDict


def getTweets (loggedUser,auth_api):
    dataJSON = {}
    i = 0
    retweeterCounter = 0
    counter = 0
    p=0
    tweetDict = {}

    for tweet in tweepy.Cursor(auth_api.user_timeline, screen_name = loggedUser.screen_name, include_rts = True).items():
        tweetDict.update({tweet.id:tweet.retweet_count})
        counter += 1
        
    print("Finished... with count: ",counter)
    sortedTweetDict = OrderedDict(sorted(tweetDict.items(), key=lambda x:x[1]))
    temp = list(sortedTweetDict.values())
    tweetRetweetNoList = temp[-3:]
    print("Retweet No of the top 3: " + str(temp[-3:]))
    temp = list(sortedTweetDict.keys())
    tweetIdList = temp[-3:]
    print("The top 3 tweets with ID: " + str(temp[-3:]))
    topThree = temp[-3:]
    print("---------------------------------------")
    while(i < 3):  
        print("Tweet no: "+ str(i) + "->" + "Printing retweeters for tweet: " +str(topThree[i]))
        retweets = auth_api.retweets(topThree[i],page=p)
        if(retweets != None): 
            for retweet in retweets:
                if(retweet):
                    try:
                        #print("USER:", retweet.user.screen_name)
                        dataJSON.update({'tweetObject' : [{'originalTweet':{'originalTweetId':tweetIdList[i],'retweetCount':tweetRetweetNoList[i]},'retweet':{'retweetCreatedAt':str(retweet.created_at),
                        'retweetId':retweet.id,'retweeterName':retweet.user.screen_name}}]})
                        #tweetList.append(retweet.user.screen_name)
                        retweeterCounter += 1
                        if(loggedUser.screen_name == 'WSJ'):
                            with open('WSJ.json','a') as file:
                                file.write(json.dumps(dataJSON,file,sort_keys=True,indent=4, separators=(',', ': ')))
                        elif(loggedUser.screen_name == 'TheHuzlers'):
                            with open('Huzzlers.json','a') as file:
                                file.write(json.dumps(dataJSON,file,sort_keys=True,indent=4, separators=(',', ': ')))
                        else:
                            print("File not found...")
                            break
                    except tweepy.TweepError:
                        print("waiting...")
                        continue
            p = p + 1
        else:
            i = i + 1
    print("Retweeters found: "+str(retweeterCounter) + " in #" +str(p) +"pages")



def PrintMembers(obj):
    for attribute in dir(obj):
        
        #We don't want to show built in methods of the class
        if not attribute.startswith('__'):
            print(attribute)
