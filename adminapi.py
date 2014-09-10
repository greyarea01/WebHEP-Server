__author__ = 'Jon'
class AdminApi:
    def  __init__(self,db):
        self.session=db.session
        self.db=db

    def getInfo(self,section,name):
        #do nothing for now
        print 'AdminApi:'+section+','+name