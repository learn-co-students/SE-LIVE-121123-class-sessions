from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

RESEARCH_FIELDS = ("AI", "Robotics", "Machine Learning", "Vision", "Cybersecurity")

db = SQLAlchemy(metadata=metadata, engine_options=({"echo": True}))


class TimestampMixin:
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


class Research(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "researches"

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String)
    year = db.Column(db.Integer)
    page_count = db.Column(db.Integer)

    research_authors = db.relationship(
        "ResearchAuthor", back_populates="research", cascade="all, delete"
    )
    authors = association_proxy("research_authors", "author")

    serialize_rules = (
        "-research_authors.research",
        "-created_at",
        "-updated_at",
    )

    @validates("year")
    def validate_year(self, key, year):
        if not len(str(year)) == 4 or not isinstance(year, int):
            raise ValueError("Year must be a four-digit integer")
        if year > datetime.now().year:
            raise ValueError("Year cannot be in the future")
        return year

    def __repr__(self):
        return f"<Research {self.topic} {self.year}>"


class Author(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    field_of_study = db.Column(db.String)

    research_authors = db.relationship(
        "ResearchAuthor", back_populates="author", cascade="all, delete"
    )

    serialize_rules = (
        "-research_authors.author",
        "-created_at",
        "-updated_at",
    )

    @validates("field_of_study")
    def validate_field_of_study(self, key, value):
        if value not in RESEARCH_FIELDS:
            raise ValueError(f"Field of study must be one of {RESEARCH_FIELDS}")
        return value


class ResearchAuthor(db.Model, TimestampMixin, SerializerMixin):
    __tablename__ = "research_authors"

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    research_id = db.Column(db.Integer, db.ForeignKey("researches.id"))

    research = db.relationship("Research", back_populates="research_authors")
    author = db.relationship("Author", back_populates="research_authors")

    serialize_rules = (
        "-research.research_authors",
        "-author.research_authors",
    )
