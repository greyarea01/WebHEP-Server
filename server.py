__author__ = 'Jon'

from peopleapi import PeopleApi
from adminapi import AdminApi
from reportapi import ReportApi
from schoolapi import SchoolApi
from dbtools import DBTools as DB

import os
import cherrypy
import sys

class App(object):
    def index(self):
        host = cherrypy.request.headers['Host']
        #realhost = cherrypy.request.headers['X-Forwarded-Host']
        realhost = 'blah'
        return 'Hello! I am ' + realhost + ' though I look like ' + host

    index.exposed = True


if __name__ == '__main__':
    argc = len(sys.argv)

    db = DB()
    if argc == 1:
        db.initDB(None)
    else:
        db.initDB(sys.argv[1])

    app = App()

    app.people = PeopleApi(db)
    app.people.exposed = True

    app.report = ReportApi(db)
    app.report.exposed = True

    app.school = SchoolApi(db)
    app.school.exposed = True

    app.admin = AdminApi(db)
    app.admin.exposed = True

    app.admin.people = PeopleApi(db,True)
    app.admin.report = ReportApi(db,True)
    app.admin.school = SchoolApi(db,True)

    app.admin.people.exposed = True
    app.admin.report.exposed = True
    app.admin.school.exposed = True

    conf = {
        '/' : {
            'tools.sessions.on' : True,
            'tools.staticdir.root' : os.path.abspath(os.getcwd())
        },
        '/admin' : {
            'tools.sessions.on' : True,
            'tools.staticdir.root' : os.path.abspath(os.getcwd())
        },
        '/people' : {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.json_in.on': True,
            'tools.json_out.on' : True,
        },
        '/report' : {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.json_in.on': True,
            'tools.json_out.on' : True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')]
        },
        '/school' : {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.json_in.on': True,
            'tools.json_out.on' : True,

            'tools.response_headers.headers': [('Content-Type', 'application/json')]
        },
        '/admin/people' : {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.json_in.on': True,
            'tools.json_out.on' : True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')]
        },
        '/admin/report' : {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.json_in.on': True,
            'tools.json_out.on' : True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')]
        },
        '/admin/school' : {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.json_in.on': True,
            'tools.json_out.on' : True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')]
        }
    }
    # FIXME check what Content-Type should be for response headers when using JSON

    cherrypy.config.update({'server.socket_port' : 8081})
    cherrypy.quickstart(app,'/',conf)
