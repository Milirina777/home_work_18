from dao.model.directors import Director

class DirectorDao:
    def __init__(self, session):
        self.session = session

# метод получения всех директоров
    def get_all(self):
        return self.session.query(Director).all()

# метод получения директора по id
    def get_one(self, uid):
        return self.session.query(Director).get(uid)
