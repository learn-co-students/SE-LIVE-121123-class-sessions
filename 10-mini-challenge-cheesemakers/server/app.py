from datetime import datetime

from flask import Flask, abort, jsonify, make_response, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import Cheese, Producer, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

Api.error_router = lambda self, handler, e: handler(
    e
)  # this workaround necessary when using an error_handler with flask-restful
api = Api(app)


@app.route("/")
def index():
    response = make_response({"message": "Hello Fromagers!"}, 200)
    return response


class Producers(Resource):
    def get(self):
        producers = [
            producer.to_dict(rules=("-cheeses",)) for producer in Producer.query.all()
        ]
        return make_response(producers, 200)


class ProducerById(Resource):
    def get(self, id):
        # producer = Producer.query.filter(Producer.id == id).first()
        # if not producer:
        #     return make_response({"error": "Resource not found"}, 404) # this avoid using errorhandler
        # return make_response(producer.to_dict(), 200)
        producer = Producer.query.get_or_404(id)
        return make_response(producer.to_dict(), 200)

    def delete(self, id):
        producer = Producer.query.get_or_404(id)
        db.session.delete(producer)
        db.session.commit()
        return make_response("", 204)


class Cheeses(Resource):
    def post(self):
        json_dict = request.get_json()
        try:
            cheese = Cheese(**json_dict)
        except ValueError as e:
            return make_response({"error": e.args}, 422)
        db.session.add(cheese)
        db.session.commit()
        return make_response(
            cheese.to_dict(
                rules=(
                    "-producer.cheeses",
                    "-producer.region",
                    "-producer.founding_year",
                    "-producer.operation_size",
                    "-producer.image",
                    "-producer.id",
                )
            ),
            201,
        )


class CheeseById(Resource):
    def patch(self, id):
        cheese = Cheese.query.get_or_404(id)
        json_dict = request.get_json()
        try:
            for key, value in json_dict.items():
                # if key == "production_date":
                #     value = datetime.strptime(value, "%Y-%m-%d")
                setattr(cheese, key, value)
        except ValueError as e:
            return make_response({"error": e.args}, 422)
        # db.session.add(cheese) ok to have this, but the cheese is already in session from the query
        db.session.commit()
        return make_response(cheese.to_dict(rules=("-producer",)), 202)

    def delete(self, id):
        cheese = Cheese.query.get_or_404(id)
        db.session.delete(cheese)
        db.session.commit()
        return make_response("", 204)


api.add_resource(Producers, "/producers")
api.add_resource(ProducerById, "/producers/<int:id>")
api.add_resource(Cheeses, "/cheeses")
api.add_resource(CheeseById, "/cheeses/<int:id>")


@app.errorhandler(404)
def handle_not_found(error):
    return make_response({"error": "Resource not found"}, 404)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
