from flask_restx import Resource, Namespace
from dao.movie_dao import MovieDao
from service.movie_service import MovieService
from dao.model.movies import MovieSchema

from setup_db import db

movies_ns = Namespace('movies')

movie_dao = MovieDao(db.session)
movie_service = MovieService(movie_dao)

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movie_service.movies_by_filters()
        return movies_schema.dump(movies), 200

    def post(self):
        updated_movie = movie_service.post_movie()
        return '', 201, {'location': f'/movies/{updated_movie.id}'}


@movies_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        movie = movie_service.get_one_movie(uid)
        return movie_schema.dump(movie), 200

    def put(self, uid):
        movie_service.put_movie(uid)
        return 'Movie information updated', 200

    def delete(self, uid):
        movie_service.delete_movie(uid)
        return 'Movie is deleted', 204
