# -*- coding: utf-8 -*-
from .databaseTable import DatabaseTable


class Users(DatabaseTable):

    def __init__(self, name):
        DatabaseTable.__init__(self, name)
