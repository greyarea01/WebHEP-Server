__author__ = 'Jon'

import cherrypy

class AdminApi:
    exposed = True

    def  __init__(self,db):
        print 'AdminAPI init'

    def index(self):
        return 'Use admin/ [people/school/report] for admin API'
