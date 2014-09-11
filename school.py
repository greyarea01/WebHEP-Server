__author__ = 'Jon'

import cherrypy

class SchoolApi:
    exposed = True

    def  __init__(self,db,admin=False):
        print 'SchoolApi init'
        self.session=db.session
        self.db=db
        self.collection = self.session.school
        self.admin = admin

    def GET(self):
        print 'GET is allowed via people API'

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
