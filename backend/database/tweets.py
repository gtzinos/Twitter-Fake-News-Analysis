from .databaseTable import DatabaseTable

class Tweets(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def find_all_by_owner_id(self, db, owner_id):
        return db[self.name].find({'owner_id': owner_id})


