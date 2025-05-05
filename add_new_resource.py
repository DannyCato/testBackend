from flask import jsonify
from flask_restful import Resource, request, reqparse
from __init__ import create_hash, add_endpoint, endpoints_contains

class add_new_resource(Resource):
    def put(self):
        endpoint: str = request.full_path
        method: str = request.method
        hash = create_hash(endpoint + method)
        # if endpoints_contains(hash):
        return {"message": endpoint + " with " + method + " method is already contained. Send DELETE first or update with POST"}, 400
        
        add_endpoint(hash, )