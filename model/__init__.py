from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from config import MysqlConfig,SqliteConfig

#DBBase = MysqlConfig.DBBase
DBBase =SqliteConfig.DBBase

#engine = create_engine(MysqlConfig.SQLALCHECHEMY_DATABASE_URI)
engine = create_engine(SqliteConfig.SQLALCHECHEMY_DATABASE_URI)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

