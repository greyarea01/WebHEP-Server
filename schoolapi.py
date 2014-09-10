__author__ = 'Jon'
class SchoolApi:
    def  __init__(self,db):
        self.session=db.session
        self.db=db

    def getInfo(self,name):
        print 'SchoolApi:'+name