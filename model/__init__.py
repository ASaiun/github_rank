from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import MysqlConfig,SqliteConfig
from sqlalchemy.orm import sessionmaker

#engine = create_engine(MysqlConfig.SQLALCHECHEMY_DATABASE_URI)
engine = create_engine(SqliteConfig.SQLALCHECHEMY_DATABASE_URI)
DBBase = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

