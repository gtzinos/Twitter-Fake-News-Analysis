import pymongo

def openConnection(hostname, dbname, port):
    connection = pymongo.MongoClient(hostname, port)
    return connection[dbname]

def closeConnection(connection):
    connection.close()