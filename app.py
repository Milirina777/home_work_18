from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db

from dao.model.directors import Director
from dao.model.genres import Genre
from dao.model.movies import Movie

from views.director import directors_ns
from views.genre import genres_ns
from views.movie import movies_ns


def create_app(config_object):
    """Функция создания основного объекта app"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)

    return app


def register_extensions(app):
    """Функция подключения расширений"""
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)

    with app.app_context():
        db.create_all()


def load_data(app, db):
    """Функция тестового заполнения"""
    with app.app_context():
        db.create_all()
        movie_1 = Movie(id=1,
                        title='Властелин колец: Братство Кольца',
                        description='Сказания о Средиземье — это хроника Великой войны за Кольцо, длившейся не одну тысячу лет. Тот, кто владел Кольцом, получал неограниченную власть, но был обязан служить злу. Тихая деревня, где живут хоббиты. Придя на 111-й день рождения к своему старому другу Бильбо Бэггинсу, волшебник Гэндальф начинает вести разговор о кольце, которое Бильбо нашел много лет назад. Это кольцо принадлежало когда-то темному властителю Средиземья Саурону, и оно дает большую власть своему обладателю. Теперь Саурон хочет вернуть себе власть над Средиземьем. Бильбо отдает Кольцо племяннику Фродо, чтобы тот отнёс его к Роковой Горе и уничтожил.',
                        trailer='123', year=2001, rating=8.6, genre_id=1, director_id=1)
        movie_2 = Movie(id=2,
                        title='Властелин колец: Возвращение короля',
                        description='Повелитель сил тьмы Саурон направляет свою бесчисленную армию под стены Минас-Тирита, крепости Последней Надежды. Он предвкушает близкую победу, но именно это мешает ему заметить две крохотные фигурки — хоббитов, приближающихся к Роковой Горе, где им предстоит уничтожить Кольцо Всевластья.',
                        trailer='456', year=2003, rating=8.7, genre_id=2, director_id=1)
        movie_3 = Movie(id=3,
                        title='Пираты Карибского моря: Проклятие Черной жемчужины',
                        description='Жизнь харизматичного авантюриста, капитана Джека Воробья, полная увлекательных приключений, резко меняется, когда его заклятый враг капитан Барбосса похищает корабль Джека Черную Жемчужину, а затем нападает на Порт Ройал и крадет прекрасную дочь губернатора Элизабет Свонн...',
                        trailer='789', year=2003, rating=8.4, genre_id=3, director_id=2)

        director_1 = Director(id=1, name='Питер Джексон')
        director_2 = Director(id=1, name='Гор Вербински')

        genre_1 = Genre(id=1, name='фэнтези')
        genre_2 = Genre(id=2, name='приключения')
        genre_3 = Genre(id=3, name='боевик')

        with db.session.begin():
            db.session.add_all([movie_1, movie_2, movie_3])
            db.session.add_all([genre_1, genre_2, genre_3])
            db.session.add_all([director_1, director_2])


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
