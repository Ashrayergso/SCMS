"""
API Documentation for Ship Crew Management System (SCMS)

This document provides a detailed description of the SCMS API endpoints.

"""

from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='SCMS API',
    description='A detailed description of the SCMS API endpoints.',
)

crew_member = api.model('Crew Member', {
    'crew_id': fields.String(required=True, description='Crew member identifier'),
    'crew_name': fields.String(required=True, description='Crew member name'),
})

@api.route('/crew_member')
class CrewMemberList(Resource):
    @api.doc('list_crew_members')
    def get(self):
        '''List all crew members'''
        pass

    @api.doc('create_crew_member')
    @api.expect(crew_member)
    def post(self):
        '''Create a new crew member'''
        pass

@api.route('/crew_member/<id>')
@api.param('id', 'The crew member identifier')
@api.response(404, 'Crew member not found')
class CrewMember(Resource):
    @api.doc('get_crew_member')
    def get(self, id):
        '''Fetch a crew member given its identifier'''
        pass

    @api.doc('delete_crew_member')
    def delete(self, id):
        '''Delete a crew member given its identifier'''
        pass

    @api.expect(crew_member)
    @api.doc('update_crew_member')
    def put(self, id):
        '''Update a crew member given its identifier'''
        pass

if __name__ == '__main__':
    app.run(debug=True)