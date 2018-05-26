import pandas as pd


class DatabaseTable:

    def __init__(self, name):
        self.name = name

    def insert_if_not_exists(self, db, id, newItem):
        exists = db[self.name].find_one({"id": id})

        if exists is None:
            try:
                db[self.name].insert(newItem)
            except Exception as e:
                print(e)

    def find_all(self, db):
        return db[self.name].find({})

    def find_count(self, db):
        return db[self.name].find({}).count()

    def toDataFrame(self, cursor):
        return pd.DataFrame(list(cursor))
