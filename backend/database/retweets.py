from .databaseTable import DatabaseTable


class Retweets(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)
