#!/usr/bin/env python

"""
craw data from github api
"""
from util.userStore import UserStore
from model import DBBase, engine


if __name__ == '__main__':
    #DBBase.metadata.create_all(engine)
    us = UserStore()
    us.user_store()

    pass