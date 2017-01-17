#!/usr/bin/env python

"""
craw data from github api
"""

from crawler.userStore import UserStore
from config import Config
# from config import config
# from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()

# engine = create_engine(config[db].SQLALCHECHEMY_DATABASE_URI)
from model import engine
import click




@click.command()
# @click.option('--db', default="default",
#               prompt="chose your db mysql or sqlite,defalut is sqlite", help="input db = mysql or sqlite")
@click.option('-ct','--create_table')

def run(create_table=None):
    # print db
    # db_init(db)
    if create_table:
        db_table_create()
    work()

# def db_init(db="default"):
#     print db
#     Config.engine = create_engine(config[db].SQLALCHECHEMY_DATABASE_URI)
#     Session.configure(bind=Config.engine)

    # Config.DBBase.metadata.create_all(Config.engine)
    # print config[db].SQLALCHECHEMY_DATABASE_URI
# @click.command()
def db_table_create():
    Config.DBBase.metadata.create_all(engine)



def work():
    us = UserStore()
    us.user_store()


if __name__ == '__main__':
    run()





