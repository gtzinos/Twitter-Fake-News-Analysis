import json
import pymongo

connection=pymongo.MongoClient(host='localhost',port=2701)
print('Connection ok')
db=connection.Twitter

print(db)
