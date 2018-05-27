from .databaseTable import DatabaseTable


class Retweets(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def find_all_not_in_followers(self, db, followers_table_name, owner_id):
        return db[self.name].aggregate([
            {
              "$match": {"retweeted_status.user.id": owner_id}
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
                                            {"$eq": ["$source.user.id", "$$userId"]},
                                            {"$eq": ["$target.user.id", "$$userId"]}
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

    def get_by_user_id(self,db, user_id, owner_id):
        return db[self.name].find_one({'user.id': user_id, "retweeted_status.user.id": owner_id})
