__author__ = 'Jon'
import cherrypy
from dbtools import DBTools as DB
import sys
from jsonpickle import encode

from schoolapi import SchoolApi
from peopleapi import PeopleApi
from reportapi import ReportApi
from adminapi import AdminApi


class Api(object):
    def __init__(self, db):
        self.schoolapi = SchoolApi(db)
        self.peopleapi = PeopleApi(db)
        self.reportapi = ReportApi(db)
        self.adminapi = AdminApi(db)

    def school(self, name):
        # do nothing
        results = self.schoolapi.getInfo(name)
        payload = encode(results, unpicklable=False)
        return payload

    school.exposed = True

    def people(self, index):
        results = self.peopleapi.getInfo(index)
        payload = encode(results, unpicklable=False)
        return payload

    people.exposed = True

    def report(self, index):
        results = self.reportapi.getInfo(index)
        payload = encode(results, unpicklable=False)
        return payload

    report.exposed = True

    def admin(self, section, name):
        results = self.adminapi.getInfo(section, name)
        payload = encode(results, unpicklable=False)
        return payload

    admin.exposed = True


class App(object):
    def index(self):
        host = cherrypy.request.header['Host']
        realhost = cherrypy.request.headers['X-Forwarded-Host']
        return 'Hello! I am ' + realhost + ' though I look like ' + host

    index.exposed = True


if __name__ == '__main__':
    argc = len(sys.argv)

    db = DB()
    if argc == 1:
        db.initDB(None)
    else:
        db.initDB(sys.argv[1])
