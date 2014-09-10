__author__ = 'Jon'
from pymongo import MongoClient

class DBTools:
    def __init__(self):
        self.db=None
        self.session = None

    def initDB(self,arg):
        self.db = MongoClient()
        self.session = self.db['WebHEP-test']
