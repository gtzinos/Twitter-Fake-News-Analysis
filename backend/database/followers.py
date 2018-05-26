from .databaseTable import DatabaseTable


class Followers(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)

    def get_last_inserted_hop(self, db, owner_id):
        return db[self.name].find({'retweeted_status.user.id': owner_id}).sort({'hop_number': -1})
