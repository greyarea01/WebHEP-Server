__author__ = 'Jon'

class PeopleApi:
    def  __init__(self,db):
        self.session=db.session
        self.db=db

    def getInfo(self,name):
        #do nothing for now
        print 'PeopleApi:'+name