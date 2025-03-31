from flask_restful import Resource, Api
from flask_cors import CORS

class add_new_resource(Resource):
    def post(self):
        