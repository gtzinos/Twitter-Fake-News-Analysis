from .databaseTable import DatabaseTable


class Followers(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def get_last_inserted_hop(self, db, owner_id):
        return db[self.name].find({'retweeted_status.user.id': owner_id}).sort([('hop_number', -1)])

    def insert_if_not_exists(self, db, newItem):
        exists = db[self.name].find_one({'source.user.id': newItem['source']['user']['id'],
                                         'target.user.id': newItem['target']['user']['id']})

        if exists is None:
            try:
                db[self.name].insert(newItem)
            except Exception as e:
                print(e)
