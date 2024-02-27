from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata, engine_options={"echo": True})


class TimestampMixin:
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


class Producer(db.Model, SerializerMixin, TimestampMixin):
    __tablename__ = "producers"

    id = db.Column(db.Integer, primary_key=True)
    founding_year = db.Column(db.Integer)
    name = db.Column(db.String)
    region = db.Column(db.String)
    operation_size = db.Column(db.String)
    image = db.Column(db.String)

    cheeses = db.relationship(
        "Cheese", back_populates="producer", cascade="all, delete"
    )
    # prevent relationship recursion with the "-cheeses.producer" rule
    serialize_rules = (
        "-cheeses.producer",
        "-created_at",
        "-updated_at",
    )

    @validates("name", "founding_year", "operation_size")
    def validate_producer_attrs(self, key, value):
        if value == "name":
            if not value:
                raise ValueError("Must have a name")
            else:  # its possible to omit the "else"; see below
                return value
        elif value == "founding_year":
            if not 1900 <= value <= 2024:
                raise ValueError("Must be between 1900 and present")
            return value
        else:
            if value not in ("small", "medium", "large", "family", "corporate"):
                raise ValueError(
                    "Must be one of small, medium, large, family or corporate"
                )
            return value

    def __repr__(self):
        return f"<Producer {self.id} | {self.name}>"


class Cheese(db.Model, SerializerMixin, TimestampMixin):
    __tablename__ = "cheeses"

    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.String)
    is_raw_milk = db.Column(db.Boolean)
    production_date = db.Column(db.DateTime)
    image = db.Column(db.String)
    price = db.Column(db.Float)

    producer_id = db.Column(db.Integer, db.ForeignKey("producers.id"), nullable=False)
    producer = db.relationship("Producer", back_populates="cheeses")

    serialize_rules = (
        "-created_at",
        "-updated_at",
    )

    @validates("price")
    def validate_price(self, key, price):
        if not 1.00 <= price <= 45.00:
            raise ValueError("Price must be between 1.00 and 45.00")
        return price

    @validates("production_date")
    def validate_production_date(self, key, date):
        production_date = datetime.strptime(date, "%Y-%m-%d")
        if production_date >= datetime.now():
            raise ValueError("Production date must be in the past")
        return production_date

    def __repr__(self):
        return f"<Cheese {self.id} | {self.kind}>"
