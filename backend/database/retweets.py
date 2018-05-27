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
                        "let": {"followerId": "$id"},
                        "pipeline": [
                            {"$match":
                                {"$expr":
                                    {"$or":
                                        [
                                            {"$eq": ["$source.retweeted_status.user.id", "$$followerId"]},
                                            {"$eq": ["$target.retweeted_status.user.id", "$$followerId"]}
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
        ]).noCursorTimeout()
