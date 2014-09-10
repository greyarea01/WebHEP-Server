__author__ = 'Jon'
class ReportApi:
    def  __init__(self,db):
        self.session=db.session
        self.db=db

    def getInfo(self,name):
        print 'ReportApi:'+name