from .databaseTable import DatabaseTable
import pymongo


class Users(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def insert_if_not_exists(self, db, loggedInUser):
        try:
            db[self.name].insert(loggedInUser._json)
        except Exception:
            pass


