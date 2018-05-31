# -*- coding: utf-8 -*-
from .databaseTable import DatabaseTable


class Retweets(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def find_all_mine(self, db, owner_id):
        return db[self.name].find({"retweeted_status.user.id": owner_id}).sort([("retweeted_status.user.id", 1)]).limit(180)

    def find_all_not_in_followers(self, db, followers_table_name, owner_id):
        return db[self.name].aggregate([
            {
                "$match": {"retweeted_status.user.id": owner_id}
            },
            {
                "$sort": {"retweeted_status.user.id": 1}
            },
            {
                "$limit": 180
            },
            {
                "$lookup":
                    {
                        "from": followers_table_name,
                        "let": {"userId": "$user.id"},
                        "pipeline": [
                            {"$match":
                                {"$expr":
                                    {"$or":
                                        [
                                            {"$eq": [
                                                "$source.user.id", "$$userId"]},
                                            {"$eq": [
                                                "$target.user.id", "$$userId"]}
                                        ]
                                     }
                                 }
                             }
                        ],
                        "as": "matched_followers"
                    }
            },
            {
                "$match": {"matched_followers": {"$eq": []}}
            }
        ])

    def get_by_user_id(self, db, user_id, owner_id):
        return db[self.name].find_one({'user.id': user_id, "retweeted_status.user.id": owner_id})

    def get_retweets_by_date(self, db, owner_id):
        return db[self.name].aggregate([
            {
                "$match": {"retweeted_status.user.id": owner_id}
            },
            {
                "$group": {
                    "_id": {"$dateToString": {"format": "%Y/%m/%d", "date": {"$dateFromString": {"dateString": "$created_at"}}}},
                    "count": {"$sum": 1}
                }
            },
            {
                "$sort": {"_id": 1}
            }
        ])
