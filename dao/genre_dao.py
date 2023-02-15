from dao.model.genres import Genre

class GenreDao:
    def __init__(self, session):
        self.session = session

# метод получения всех жанров
    def get_all(self):
        return self.session.query(Genre).all()

# метод получения жанра по id
    def get_one(self, uid):
        return self.session.query(Genre).get(uid)
