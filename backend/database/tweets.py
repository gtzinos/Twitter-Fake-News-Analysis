# -*- coding: utf-8 -*-
from .databaseTable import DatabaseTable


class Tweets(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def find_all_by_owner_id(self, db, owner_id):
        return db[self.name].find({'user.id': owner_id})

    def find_top_3(self, db, owner_id):
        return db[self.name].find({'user.id': owner_id}).sort([("retweet_count", -1)]).limit(3)
    