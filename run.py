#!/usr/bin/env python

"""
craw data from github api
"""
from config import Config
from crawler.crawUser import CrawUser
from model import session
from model.userData import User


def main():
    c = CrawUser(Config)
    i = 0
    n = 0

    flag = True
    while (flag):
        for uj in c.get_id_user_data(n):
            i += 1
            # print i, uj.get("id")
            user = User(uj.get("id"), uj.get("login"), uj.get("avatar_url"), uj.get("gravatar_id"), uj.get("url"),
                        uj.get("html_url"), uj.get("followers_url"), uj.get("following_url"), uj.get("gists_url"),
                        uj.get("starred_url"), uj.get("subscriptions_url"), uj.get("organizations_url"),
                        uj.get("repos_url"), uj.get("events_url"), uj.get("received_events_url"), uj.get("type"),
                        uj.get("site_admin"), uj.get("name"), uj.get("company"), uj.get("blog"), uj.get("location"),
                        uj.get("email"), uj.get("hireable"), uj.get("bio"),
                        uj.get("public_repos"), uj.get("public_gists"), uj.get("followers"),
                        uj.get("following"), uj.get("created_at"), uj.get("updated_at"))
            session.add(user)
            session.commit()

            if uj.get("id") is None:
                flag = False

            if i == 30:
                i = 0
                n = uj.get("id")


                # c.get_user_data()
                # c.get_id_user_data(5)
                # c.get_all_user_data()
                # c.get_id_user_data()

                # app.run()



                #
                # from flask import Flask
                # from flask_sqlalchemy import SQLAlchemy
                #
                # app = Flask(__name__)
                # app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@127.0.0.1:3306/github_rank"
                # db = SQLAlchemy(app)
                #
                #
                # class User(db.Model):
                #     id = db.Column(db.Integer, primary_key=True)
                #     username = db.Column(db.String(80), unique=True)
                #     email = db.Column(db.String(120), unique=True)
                #
                #     def __init__(self, username, email):
                #         self.username = username
                #         self.email = email
                #
                #     def __repr__(self):
                #         return '<User %r>' % self.username
                #
                #
                # if __name__ == '__main__':
                #     db.create_all()


if __name__ == '__main__':
    main()
