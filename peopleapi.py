__author__ = 'Jon'

import cherrypy

class PeopleApi:
    exposed = True

    def  __init__(self,db,admin=False):
        print 'PeopleAPI init'
        self.session=db.session
        self.db=db
        self.collection = self.session.people
        self.admin = admin

    def GET(self,*args):
        # retrieve an item
        print 'GET is allowed via people API'
        for arg in args:
            print arg

    def PUT(self):
        if self.admin:
            print 'PUT is allowed via admin interface'
        else:
            print 'PUT not allowed via people API'
    def POST(self):
        if self.admin:
            print 'POST is allowed via admin API'
        else:
            print 'POST not allowed via people API'

    def DELETE(self):
        if self.admin:
            print 'DELETE not allowed via people API'
        else:
            print 'DELETE not allowed via people API'
