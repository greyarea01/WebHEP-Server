__author__ = 'Jon'

import cherrypy

class PeopleApi:
    exposed = True

    def  __init__(self,db,admin=False):
        print 'PeopleAPI init'
        self.db=db
        self.admin = admin
    def GET(self,index=None):
        # retrieve an item
        # GET /api/people - get all people
        # GET /api/people/:id - get one person if they exist
        print 'GET is allowed via people API'
        if index != None:
            result = self.db.retrieve('people', { '_id' : index})
        else:
            result = []
        print result
        return result

    def PUT(self,index=None):
        # put UPDATE item - CREATE not allowed
        # PUT /api/people/ not allowed
        # PUT /api/people/:id - update record with _id = id
        record = cherrypy.request.json
        print record
        if self.admin:
            print 'PUT is allowed via admin interface'
            if record != None:
                if index == record._id:
                    result = self.db.update('people',record)
                    print result
        else:
            print 'PUT not allowed via people API'
            raise cherrypy.HTTPError("403 Forbidden", "Only admin may update")

    def POST(self,record=None):
        # CREATE a new item
        # POST /api/people/ create a new item and return it
        # POST /api/people/:id not allowed
        if self.admin:
            print 'POST is allowed via admin API'
            if record != None:
                result = self.db.update('people',record)
                print result
        else:
            print 'POST not allowed via people API'
            raise cherrypy.HTTPError("403 Forbidden", "Only admin may create")

    def DELETE(self):
        # remove a person
        # DELETE /api/people - not allowed
        # DELETE /api/people/:id - remove the person with _id = id
        if self.admin:
            print 'DELETE not allowed via people API'
        else:
            print 'DELETE not allowed via people API'
            raise cherrypy.HTTPError("403 Forbidden", "Only admin may delete")
