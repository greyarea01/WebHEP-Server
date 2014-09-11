__author__ = 'Jon'
from pymongo import MongoClient

class DBTools:
    def __init__(self):
        self.db=None
        self.session = None

    def initDB(self,arg):
        self.db = MongoClient()
        self.session = self.db['WebHEP-test']

# provide CRUD interface
    def create(self,collectionName,object):
        collection = self.session[collectionName]
        object._id = self.getNextSequence(collectionName)
        return collection.insert(object)

    def retrieve(self,collectionName,query):
        collection = self.session[collectionName]
        return collection.find(query)

    def update(self,collectionName, object):
        collection = self.session[collectionName]
        # check to see if the object exists
        # since we can't just set the upsert flag since we need to
        # increment the sequence number to generate a valid id
        result = collection.find_one( { '_id' : object._id}, { '_id' : 1})
        if result==None:
            return self.create(collectionName,object)
        else:
            return collection.findAndModify( {'_id' : object._id},object)

    def delete(self,collectionName,query):
        collection = self.session[collectionName]
        # second argument specifies only ever remove one document
        return collection.remove(query, True)

# generate sequence numbers for a collection
    def getNextSequence(self, collectionName):
        collection = self.session['counters']
        # upsert a new index number each time we create a new entry
        collection.findAndModify( {
            'query' : { '_id' : collectionName},
            'update' : { '$inc' : { 'seq' : 1} },
            'new' : True,
            'upsert' : True
        })