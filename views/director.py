from flask_restx import Namespace, Resource
from dao.director_dao import DirectorDao
from dao.model.directors import DirectorSchema
from service.director_service import DirectorService
from setup_db import db

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

director_dao = DirectorDao(db.session)
director_service = DirectorService(director_dao)

@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_directors()
        return directors_schema.dump(directors), 200


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid):
        director = director_service.get_director(uid)
        return director_schema.dump(director), 200
