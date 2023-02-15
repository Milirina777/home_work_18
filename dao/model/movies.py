from setup_db import db
from marshmallow import Schema, fields

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    trailer = db.Column(db.String())
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genres = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    directors = db.relationship("Director")


class MovieSchema(Schema):

    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
