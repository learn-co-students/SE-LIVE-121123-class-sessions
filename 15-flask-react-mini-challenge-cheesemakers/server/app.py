from datetime import datetime

from flask import Flask, abort, jsonify, make_response, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import Cheese, Producer, db
from werkzeug.exceptions import NotFound

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

Api.error_router = lambda self, handler, error: handler(error)
api = Api(app)


class Producers(Resource):
    def get(self):
        producers = [prod.to_dict(rules=("-cheeses",)) for prod in Producer.query.all()]
        return make_response(producers, 200)


class ProducersById(Resource):
    def get(self, id):
        producer = Producer.query.filter(Producer.id == id).first()
        if not producer:
            abort(404, "Producer not found")
        return make_response(producer.to_dict(), 200)

    def delete(self, id):
        producer = Producer.query.filter(Producer.id == id).first()
        if not producer:
            abort(404, "Producer not found")
        db.session.delete(producer)
        db.session.commit()
        return make_response("", 204)


class Cheeses(Resource):
    def post(self):
        cheese_JSON = request.get_json()
        print(cheese_JSON)
        try:
            new_cheese = Cheese(**cheese_JSON)
            # new_cheese.production_date = datetime.strptime(
            #     cheese_JSON["production_date"], "%Y-%m-%d"
            # )
        except ValueError as e:
            return make_response({"error": e.args}, 422)
        db.session.add(new_cheese)
        db.session.commit()
        return make_response(
            new_cheese.to_dict(
                rules=(
                    "-producer.founding_year",
                    "-producer.region",
                    "-producer.operation_size",
                    "-producer.image",
                    "-producer.id",
                )
            ),
            201,
        )


class CheesesById(Resource):
    def patch(self, id):
        cheese = Cheese.query.filter(Cheese.id == id).first()
        if not cheese:
            raise NotFound
        data = request.get_json()
        try:
            for key, value in data.items():
                setattr(cheese, key, value)
            db.session.commit()
        except ValueError as e:
            return make_response({"error": e.args}, 422)

        return make_response(cheese.to_dict(rules=("-producer",)), 200)

    def delete(self, id):
        cheese = Cheese.query.filter(Cheese.id == id).first()
        if not cheese:
            raise NotFound
        db.session.delete(cheese)
        db.session.commit()
        return make_response("", 204)


api.add_resource(Producers, "/producers")
api.add_resource(ProducersById, "/producers/<int:id>")
api.add_resource(Cheeses, "/cheeses")
api.add_resource(CheesesById, "/cheeses/<int:id>")


@app.errorhandler(NotFound)
def handle_not_found(error):
    return make_response({"error": error.args}, 404)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
