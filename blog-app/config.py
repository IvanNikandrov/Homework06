from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://username:passwd!@localhost:5431/blog"
)


class Config:
    DEBUG = False
    TESTING = False
    ENV = 'development'

    SECRET_KEY = "qwertytrewsupersecret"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

class TestingConfig(Config):
    DEBUG = True
    TESTING = True

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    ENV = 'production'
    SECRET_KEY = 'dsflghsdflkmoifgy7da932822938jrf'