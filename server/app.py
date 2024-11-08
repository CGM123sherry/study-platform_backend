from flask import jsonify, make_response
from flask_restful import Resource
from config import app, api
from models import Users

class HomeResource(Resource):
    def get(self):
        return make_response(jsonify({"message":"Welcome to the Api"}), 200)
api.add_resource(HomeResource,"/api")

if __name__=="__main__":
    app.run(debug=True)
