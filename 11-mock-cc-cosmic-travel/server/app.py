#!/usr/bin/env python3

import os

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import Mission, Planet, Scientist, db

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

api = Api(app)

db.init_app(app)


# @app.route('/')
# def home():
#     return 'Welcome to Cosmic Travel'

class Scientists(Resource):
    def get(self):
        scientists =  [scientist.to_dict(rules=("-missions",)) for scientist in Scientist.query.all()]
        return make_response(scientists, 200)

    def post(self):
        req_data = request.get_json()
        try:
            new_scientist = Scientist(**req_data)
        except ValueError as e:
            return make_response({"errors": ['validation errors']}, 400)
        db.session.add(new_scientist)
        db.session.commit()
        return make_response(new_scientist.to_dict(), 201)
    
class ScientistById(Resource):
    def get(self, id):
        scientist = Scientist.query.get_or_404(id, description="Scientist not found")
        # if not scientist:
        #     return make_response({"error": "Scientist not found"}, 404)
        return make_response(scientist.to_dict(), 200)
    
    def delete(self, id):
        scientist = Scientist.query.filter(Scientist.id==id).first()
        if not scientist:
            return make_response({"error": "Scientist not found"}, 404)
        db.session.delete(scientist)
        db.session.commit()
        return make_response({}, 204)

    def patch(self, id):
        scientist = Scientist.query.filter(Scientist.id==id).first()
        # scientist = Scientist.query.get_or_404(id)
        req_data = request.get_json()
        if not scientist:
            return make_response({"error": "Scientist not found"}, 404)
        try:
            for key, value in req_data.items():
                setattr(scientist, key, value)
        except:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.commit()
        return make_response(scientist.to_dict(), 202)

class Planets(Resource):
    def get(self):
        planets = [planet.to_dict(rules=("-missions",)) for planet in Planet.query.all()]
        return make_response(planets, 200)
    
class Missions(Resource):
    def post(self):
        req_data = request.get_json()
        try:
            new_mission = Mission(**req_data)
        except:
            return make_response({"errors": ["validation errors"]}, 400)
        db.session.add(new_mission)
        db.session.commit()
        return make_response(new_mission.to_dict(), 201)

    
api.add_resource(Scientists, "/scientists")
api.add_resource(ScientistById, "/scientists/<int:id>")
api.add_resource(Planets, "/planets")
api.add_resource(Missions, "/missions")

if __name__ == '__main__':
    app.run(port=5555, debug=True)
