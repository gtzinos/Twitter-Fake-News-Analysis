import tweepy
from tweepy import *
import csv
import json
import pprint
import re
from collections import OrderedDict

def getTweetsHuzlers(loggedUser,auth_api):
    filePath = './user/h.json'
    dataHuzlersJSON = {}
    i = 0
    retweeterCounter = 0
    counter = 0
    p=0
    tweetDict = {}
    tweeters = {}

    for tweet in tweepy.Cursor(auth_api.user_timeline, screen_name = loggedUser.screen_name, include_rts = True).items():
        tweeters.update({tweet.id:tweet.user.id})
        tweetDict.update({tweet.id:tweet.retweet_count})
        counter += 1
        
    print("Finished... with count: ",counter)
    #At the time of collection the tweet with the smallest retweet count gave no results so we took the one before it
    #and drop the other from the list
    print("Printing info: ...")
    sortedTweetersDict = OrderedDict(sorted(tweeters.items(), key=lambda x:x[1]))
    tempTweeters = list(sortedTweetersDict.values())
    tweetersTop = tempTweeters[-5:]
    del tweetersTop[1:3]
    print("Original tweeters of the top 3: "+str(tweetersTop))
    sortedTweetDict = OrderedDict(sorted(tweetDict.items(), key=lambda x:x[1]))
    temp = list(sortedTweetDict.values())
    tweetRetweetNoList = temp[-5:]
    del tweetRetweetNoList[1:3]
    print("Retweet No of the top 3: " + str(tweetRetweetNoList))
    temp = list(sortedTweetDict.keys())
    tweetIdList = temp[-5:]
    del tweetIdList[1:3]
    print("The top 3 tweets with ID: " + str(tweetIdList))
    topThree = temp[-5:]
    del topThree[1:3]
    print("---------------------------------------")
    while(i < 3):  
        print("Tweet no: "+ str(i) + "->" + "Printing retweeters for tweet: " +str(topThree[i]))
        try:
            retweets = auth_api.retweets(topThree[i],page=p)
            
            if(retweets != None): 
                for retweet in retweets:
                    if(retweet):
                        try:
                            #print("USER:", retweet.user.screen_name)
                            dataHuzlersJSON.update({'tweetObject' : [{'originalTweet':{'originalTweetId':tweetIdList[i],'retweetCount':tweetRetweetNoList[i],'originalTweeter':tweetersTop[i]},'retweet':{'retweetCreatedAt':str(retweet.created_at),
                            'retweetId':retweet.id,'retweeterName':retweet.user.screen_name}}]})
                            #tweetList.append(retweet.user.screen_name)
                            retweeterCounter += 1
                            with open(filePath,'a') as fileh:
                                json.dump(dataHuzlersJSON, fileh, sort_keys=True, indent=4,ensure_ascii=False)
                            fileh.close
                            print("waiting...")
                            continue
                        except TweepError as e:
                            print("TweepError")
                            print(str(e))
                            continue
                        except Exception as e:
                            print("Exceptions 1")
                            print(str(e))
                            continue
                
                p = p + 1
            else:
                i = i + 1
        except Exception as e:
            print("Exceptions 2")
            print(str(e))
            continue
    print("Retweeters found: "+str(retweeterCounter) + " in #" +str(p) +"pages")



def PrintMembers(obj):
    for attribute in dir(obj):
        
        #We don't want to show built in methods of the class
        if not attribute.startswith('__'):
            print(attribute)

#Filter text characters to utf8 and remove spaces
def filterText(text):
    text = str(u''.join(text).encode('utf-8'))
    text = text.replace("\n", "")
    text = text.replace('"', "'")
    text = re.sub(r"^[ ]+", "", text)
    text = re.sub(r"[ ]+$", "", text)
    return text
