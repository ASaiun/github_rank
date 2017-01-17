from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from config import Config

DBBase = declarative_base()

engine = create_engine(Config.SQLALCHECHEMY_DATABASE_URI)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

