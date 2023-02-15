from flask_restx import Namespace, Resource
from service.genre_service import GenreService
from dao.genre_dao import GenreDao
from dao.model.genres import GenreSchema
from setup_db import db

genres_ns = Namespace('genres')

genre_dao = GenreDao(db.session)
genre_service = GenreService(genre_dao)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genres_ns.route('/')
class GenresView(Resource):

    def get(self):
        genres = genre_service.get_genres()
        return genres_schema.dump(genres), 200


@genres_ns.route('/<int:uid>')
class GenreView(Resource):

    def get(self, uid):
        genre = genre_service.get_genre(uid)
        return genre_schema.dump(genre), 200
