import pymongo


def openConnection(hostname, dbname, port, username, password, authMechanism):
    connection = pymongo.MongoClient(hostname, port, username=username, password=password,
                                     authSource=dbname, authMechanism=authMechanism)

    return connection[dbname]


def closeConnection(connection):
    connection.close()
