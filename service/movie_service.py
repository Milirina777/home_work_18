from flask import request
from dao.model.movies import Movie
from setup_db import db


class MovieService:
    def __init__(self, m_dao):
        self.m_dao = m_dao

    def get_all_movies(self):
        """Получение всех фильмов"""
        return self.m_dao.get_all()

    def get_one_movie(self, uid):
        """Получение фильма по id"""
        return self.m_dao.get_one(uid)

    def put_movie(self, uid):
        """Изменение фильма """
        req_json = request.json
        movie_update = db.session.query(Movie).get(uid)
        movie_update.name = req_json.get('name')
        movie_update.title = req_json.get('title')
        movie_update.description = req_json.get('description')
        movie_update.trailer = req_json.get('trailer')
        movie_update.year = req_json.get('year')
        movie_update.rating = req_json.get('rating')
        movie_update.genre_id = req_json.get('genre_id')
        movie_update.director_id = req_json.get('director_id')
        self.m_dao.put_dao_movie(movie_update)

        return 'Movie information updated'

    def post_movie(self):
        """Добавление фильма или создание фильма"""
        req_json = request.json
        req_json.pop('id', None)
        try:
            movie = Movie(**req_json)
            self.m_dao.post_movie(movie)
        except Exception:
            return 'Failed to insert information', 400

        return self.m_dao.post_dao_movie()

    def movies_by_filters(self):
        """Фильмы через фильтры"""

        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')

        if director_id is not None:
            movie = self.m_dao.get_by_director_id(director_id)
        elif genre_id is not None:
            movie = self.m_dao.get_by_genre_id(genre_id)
        elif year is not None:
            movie = self.m_dao.get_by_year(year)
        else:
            movie = self.m_dao.get_all()
        return movie

    def delete_movie(self, uid):
        """Удаление фильма по id"""
        movie_delete = db.session.query(Movie).get(uid)
        self.m_dao.delete_dao_movie(movie_delete)
        return 'Movie is deleted', 204
