class GenreService:
    def __init__(self, genre_dao):
        self.genre_dao = genre_dao

    def get_genres(self):
        """Получение всех"""
        return self.genre_dao.get_all()

    def get_genre(self, uid):
        """Получение по id"""
        return self.genre_dao.get_one(uid)
