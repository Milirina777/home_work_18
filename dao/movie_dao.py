from dao.model.movies import Movie

class MovieDao:
    def __init__(self, session):
        self.session = session

# метод получения всех фильмов
    def get_all(self):
        return self.session.query(Movie).all()

# метод получения фильма по id
    def get_one(self, uid):
        return self.session.query(Movie).get(uid)

# метод получения по id директора
    def get_by_director_id(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

# метод получения по id жанра
    def get_by_genre_id(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

# метод получения по году
    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

# метод создания фильма
    def post_dao_movie(self, movie):
        self.session.add(movie)
        self.session.commit(movie)
        return 'Movie is created', 201

# метод удаления фильма
    def delete_dao_movie(self, movie):
        self.session.delete(movie)
        self.session.commit()
        self.session.close()

# метод изменения информации о фильме
    def put_dao_movie(self, movie):
        self.session.add(movie)
        self.session.commit()
        self.session.close()
