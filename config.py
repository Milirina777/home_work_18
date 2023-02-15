# Это файл конфигурации приложения

class Config(object):
    DEBUG = True
    SECRET_HERE = 'HW18'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
