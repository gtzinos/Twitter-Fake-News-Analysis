import json
import pymongo
import sys
import os

## Insert json files into mongo db
def insertData():
    connection=pymongo.MongoClient(host='localhost',port=27017)
    print('Connection ok')

    db=connection.sna

    retweets_h=db.retweet_h
    retweets_w=db.retweet_w

    current_work_directory = os.getcwd() 

    for i in range(1,4):
        data=open(current_work_directory + '/user/data/h_'+str(i)+'.json','r')
        parsed=json.loads(data.read())
        retweets_h.insert(parsed)
        print('Document h_'+str(i)+'.json insterted!')

    for i in range(1,4):
        data=open(current_work_directory + '/user/data/w_'+str(i)+'.json','r')
        parsed=json.loads(data.read())
        retweets_w.insert(parsed)
        print('Document w_'+str(i)+'.json insterted!')

    print('All documents inserted successfuly!')