import os

from sqlalchemy.ext.declarative import declarative_base

basedir = os.path.abspath(os.path.dirname(__file__))



class Config:

    # engine = None
    DBBase = declarative_base()
    GITHUB_USER = os.environ.get('GITHUB_USER')
    GITHUB_PASSWORD = os.environ.get('GITHUB_PASSWORD')
    BASE_URL = 'https://api.github.com'



class MysqlConfig(Config):
    SQLALCHECHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/github_rank"


class SqliteConfig(Config):
    SQLALCHECHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'data.sqlite')


# config = {
#     'mysql': MysqlConfig,
#     'sqlite': SqliteConfig,
#
#     'default': MysqlConfig
#     #'default': SqliteConfig
# }