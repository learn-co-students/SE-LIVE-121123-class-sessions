from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
# Configure the database URI
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pet_app.db"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pet_app.db"


# Initialize Flask-SQLAlchemy
db = SQLAlchemy()
db.init_app(app)
# Initialize Flask-Migrate
migrate = Migrate(app, db)
