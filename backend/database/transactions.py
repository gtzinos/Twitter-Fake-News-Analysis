import json
import pymongo
import sys
import os
import pprint as pp


## Insert json files into mongo db
def insertData():
    connection = pymongo.MongoClient(host='localhost', port=27017)
    print('Connection ok')

    db = connection.sna

    retweets_h = db.retweet_h
    retweets_w = db.retweet_w

    current_work_directory = os.getcwd()

    for i in range(1, 4):
        data = open(current_work_directory + '/user/data/h_' + str(i) + '.json', 'r')
        parsed = json.loads(data.read())
        retweets_h.insert(parsed)
        print('Document h_' + str(i) + '.json insterted!')

    for i in range(1, 4):
        data = open(current_work_directory + '/user/data/w_' + str(i) + '.json', 'r')
        parsed = json.loads(data.read())
        retweets_w.insert(parsed)
        print('Document w_' + str(i) + '.json insterted!')

    print('All documents inserted successfuly!')


def showData():
    connection = pymongo.MongoClient(host='localhost', port=27017)
    print('Connection ok')

    db = connection.sna
    calHuz = db.retweet_h
    calWsj = db.retweet_w

    pp.pprint(db.collection_names(include_system_collections=False))

    print('Total items in retweet_h collection: ' + str(calHuz.count()))
    print('Total items in retweet_w collection: ' + str(calWsj.count()))

    # for tweet in calHuz.find():
    #   pp.pprint(tweet.retweeterName)

    for tweet in calHuz.find({}, ):
        print(tweet)
