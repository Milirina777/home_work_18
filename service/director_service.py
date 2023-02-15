class DirectorService:
    def __init__(self, director_dao):
        self.director_dao = director_dao

    def get_directors(self):
        """Получение всех"""
        return self.director_dao.get_all()

    def get_director(self, uid):
        """Получение по id"""
        return self.director_dao.get_one(uid)
