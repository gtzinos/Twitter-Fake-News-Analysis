from .databaseTable import DatabaseTable


class Followers(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def get_last_inserted_hop(self, db, owner_id):
        results = db[self.name].aggregate([
            {
                "$match": {
                    "from_owner.id": owner_id
                }
            },
            {
                "$group": {
                    "_id": "$hop_number",
                    "results": {"$push": "$$ROOT"}
                }
            },
            {
                "$sort": {"_id": -1}
            },
            {
                "$limit": 1
            }
        ]).next()['results']

        return results

    def insert_if_not_exists(self, db, newItem):
        exists = db[self.name].find_one({'source.user.id': newItem['source']['user']['id'],
                                         'target.user.id': newItem['target']['user']['id']})

        if exists is None:
            try:
                db[self.name].insert(newItem)
            except Exception as e:
                print(e)

    def get_my_followers(self, db, owner_id):
        return db[self.name].find({"from_owner.id": owner_id}).sort([("hop_number", 1)])

    def get_tweets_by_hop(self, db, owner_id, retweets_table_name):

        return db[self.name].aggregate([
            {
                "$match": {"from_owner.id": owner_id}
            },
            {
                "$lookup":
                    {
                        "from": retweets_table_name,
                        "let": {"sourceUserId": "$source.user.id"},
                        "pipeline": [
                            {"$match":
                             {"$expr":
                              {"$or":
                               [
                                   {"$eq": ["$user.id", "$$sourceUserId"]}
                               ]
                               }
                              }
                             }
                        ],
                        "as": "matched_followers"
                    }
            },
            {
                "$group": {
                    "_id": "$hop_number",
                    "count": {"$sum": {"$size": "$matched_followers"}}
                }
            },
            {
                    "$sort": {'_id': 1}
            }
        ])
