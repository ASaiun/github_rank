#!/usr/bin/env python

"""
craw data from github api
"""
from model.userData import DBBase
from model import engine
import click


@click.group()
def cli():
    pass


@cli.command()
def db():
    DBBase.metadata.create_all(engine)


@cli.command()
def crawler():
    from crawler.user import CrawlUser
    crawl_user = CrawlUser()
    crawl_user.start() # only one task


if __name__ == '__main__':
    cli()
