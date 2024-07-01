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
    updated_at = db.Column(db.DateTime, server_onupdate=db.func.now())


class Producer(db.Model, SerializerMixin, TimestampMixin):
    __tablename__ = "producers"

    id = db.Column(db.Integer, primary_key=True)
    founding_year = db.Column(db.Integer)
    name = db.Column(db.String, nullable=False)
    region = db.Column(db.String)
    operation_size = db.Column(db.String)
    image = db.Column(db.String)

    cheeses = db.relationship("Cheese", back_populates="producer", cascade="delete")

    serialize_rules = (
        "-cheeses.producer",
        "-updated_at",
        "-created_at",
    )

    @validates("founding_year")
    def validate_founding_year(self, key, year):
        import ipdb

        # ipdb.set_trace()
        if not 1900 < year < int(datetime.now().year):
            raise ValueError("Founding year must be between 1900 and present")
        return year

    @validates("operation_size")
    def validate_operation_size(self, key, size):
        OP_SIZE = ["small", "medium", "large", "family", "corporate"]
        if size not in OP_SIZE:
            raise ValueError(
                "Operation size must be one of small, medium, large, family, corporate"
            )
        return size

    def __repr__(self):
        return f"<Producer {self.id}>"


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
        "-producer.cheeses",
        "-updated_at",
        "-created_at",
    )

    @validates("production_date")
    def validate_production_date(self, key, date):
        import ipdb

        # ipdb.set_trace()
        pdate = datetime.strptime(date, "%Y-%m-%d")
        if pdate.date() >= datetime.now().date():
            raise ValueError("Production date must be in the past")
        return pdate

    @validates("price")
    def validate_price(self, key, price):
        if not 1.00 <= price <= 45.00:
            raise ValueError("Price must be between 1.00 and 45.00")
        return price

    def __repr__(self):
        return f"<Cheese {self.id}>"
