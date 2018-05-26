import tweepy

from config.credentials import *
from config.database import *
import os
import json

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

current_work_directory = os.getcwd()


file_path="./user/data/hop1/"

hop1={}
hop2={}
hop3={}

#returns true or false 
def checkFriendship(originalTweeterId,target_user):
    status=api.show_friendship(source_id=originalTweeterId, target_screen_name=target_user)
    #print('Full object:')
    #pp.pprint(status)
    #print('Following A, Following B')
    #print(status[0].following,status[1].following)
    #if status[0].following == False & status[0].following == False 
     #   print("Not following")
    #else:
     #   print("Following")
    print("user a followed by user "+str(target_user)+": "+str(status[0].followed_by))
    return status[0].followed_by 
    #print("user a following user b: "+str(status[0].following))
    #print("user b followed by user a: "+str(status[1].followed_by))
    #print("user b following user a: "+str(status[1].following))

def readDataFromJSON(file_name):
    retweeters=[]
    with open(current_work_directory + '/user/data/'+file_name,'r') as f:
        data=json.load(f)
        length=len(data)
        originalTweeterId=data[0]["tweetObject"][0]["originalTweet"]["originalTweeter"]        
        for i in range(0,length):
            retweeters.append(str(data[i]["tweetObject"][0]["retweet"]["retweeterName"]))
            #print("Retweeter name: "+str(data[i]["tweetObject"][0]["retweet"]["retweeterName"]))
            #print(str(i))
    #print("Retwewters count: "+str(len(retweeters))
    #print("Original Tweeter ID:"+str(originalTweeterId))
    print("A tweet from user with id= "+str(originalTweeterId)+" has retweeted "+str(len(retweeters))+" times.")
    print()
    print("Searching for direct users of "+str(originalTweeterId)+" id.")

    followers={}

    nonFollowers={}


    if(retweeters != None):
        try:
            for user in range(0,len(retweeters)):
                try:
                    isFollower = checkFriendship(originalTweeterId,retweeters[user])
                    if(isFollower):
                        followers.update({'user':retweeters[user]})

                        with open(current_work_directory+"/user/data/hop_1/hop1_first_tweet.json",'a') as fileh:
                            json.dump(followers, fileh, sort_keys=True, indent=4,ensure_ascii=False)
                        fileh.close
                    else:
                        nonFollowers.update({'user':retweeters[user]})
                        with open(current_work_directory+"/user/data/hop_1/hop1_left_users.json",'a') as file2:
                            json.dump(nonFollowers, file2, sort_keys=True, indent=4,ensure_ascii=False)
                        file2.close

                except tweepy.TweepError as er:
                    print("Tweepy Error: "+str(er))
            
        except Exception as ex:
            print("Error: "+str(ex))
    else:
        print("There is no retweeter!")

    
    print("Followers of original tweeter: "+str(len(followers)))
    print()
    for i in range(0,len(followers)):
        print(followers[i])

    print("Non followers of original tweeter: "+str(len(nonFollowers)))
    print()
    #for i in range(0,len(followers)):
     #   print(followers[i])
    