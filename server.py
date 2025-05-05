from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from add_new_resource import *

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(add_new_resource, "/")

# add support for args 
def main():
    print("Starting flask")
    app.run(debug=True),

if __name__ == '__main__':
    main()
