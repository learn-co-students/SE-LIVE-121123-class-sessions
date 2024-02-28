#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import Author, Research, ResearchAuthor, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)


# @app.route("/")
# def index():
#     return "<h1>Code challenge</h1>"


class Researches(Resource):
    def get(self):
        researches = [
            r.to_dict(rules=("-research_authors",)) for r in Research.query.all()
        ]
        return make_response(researches, 200)


class ResearchById(Resource):
    def get(self, id):
        research = Research.query.filter(Research.id == id).first()
        if not research:
            return make_response({"error": "Research paper not found"}, 404)
        return make_response(
            research.to_dict(
                rules=(
                    "authors",
                    "-authors.research_authors",
                    "-research_authors",
                )
            ),
            200,
        )

    def delete(self, id):
        research = Research.query.filter(Research.id == id).first()
        if not research:
            return make_response({"error": "Research paper not found"}, 404)
        db.session.delete(research)
        db.session.commit()
        return make_response({}, 204)


api.add_resource(Researches, "/research")
api.add_resource(ResearchById, "/research/<int:id>")

if __name__ == "__main__":
    app.run(port=5555, debug=True)
