#!/usr/bin/env python

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from config import Config
from crawler.crawUser import CrawUser
from flask_sqlalchemy import SQLAlchemy

"""
craw data from github api
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    Config.SQLALCHECHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config[' SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# manager = Manager(app)

db = SQLAlchemy(app)


# db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64))
    avatar_url = db.Column(db.String(128))
    gravatar_id = db.Column(db.String(64))
    url = db.Column(db.String(128))
    html_url = db.Column(db.String(128))
    followers_url = db.Column(db.String(128))
    following_url = db.Column(db.String(128))
    gists_url = db.Column(db.String(128))
    starred_url = db.Column(db.String(128))
    subscriptions_url = db.Column(db.String(128))
    organizations_url = db.Column(db.String(128))
    repos_url = db.Column(db.String(128))
    events_url = db.Column(db.String(128))
    received_events_url = db.Column(db.String(128))
    type = db.Column(db.String(64))
    site_admin = db.Column(db.Boolean)
    name = db.Column(db.String(64))
    company = db.Column(db.String(128))
    blog = db.Column(db.String(128))
    location = db.Column(db.String(128))
    email = db.Column(db.String(128))
    hireable = db.Column(db.Boolean)
    bio = db.Column(db.String(128))
    public_repos = db.Column(db.Integer)
    public_gists = db.Column(db.Integer)
    followers = db.Column(db.Integer)
    following = db.Column(db.Integer)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())

    def __init__(self, id, login, avatar_url, gravatar_id, url,
                 html_url, followers_url, following_url, gists_url,
                 starred_url, subscriptions_url, organizations_url,
                 repos_url, events_url, received_events_url, type,
                 site_admin, name=None, company=None, blog=None, location=None, email=None, hireable=None, bio=None,
                 public_repos=None, public_gists=None, followers=None, following=None, created_at=None,
                 updated_at=None):
        self.id = id
        self.login = login
        self.avatar_url = avatar_url
        self.gravatar_id = gravatar_id
        self.url = url
        self.html_url = html_url
        self.followers_url = followers_url
        self.following_url = following_url
        self.gists_url = gists_url
        self.starred_url = starred_url
        self.starred_url = starred_url
        self.subscriptions_url = subscriptions_url
        self.organizations_url = organizations_url
        self.repos_url = repos_url
        self.events_url = events_url
        self.received_events_url = received_events_url
        self.type = type
        self.site_admin = site_admin
        self.name = name
        self.company = company
        self.blog = blog
        self.location = location
        self.email = email
        self.hireable = hireable
        self.bio = bio
        self.public_repos = public_repos
        self.public_gists = public_gists
        self.followers = followers
        self.following = following
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<Users %r>' % self.name


if __name__ == '__main__':
    # db.create_all()
    # manager.run()

    c = CrawUser(Config)
    i = 0
    n = 0

    flag = True
    while (flag):
        for uj in c.get_id_user_data(n):
            i = i + 1
            # print i, uj.get("id")
            user = User(uj.get("id"),uj.get("login"),uj.get("avatar_url"),uj.get("gravatar_id"),uj.get("url"),
                        uj.get("html_url"),uj.get("followers_url"),uj.get("following_url"),uj.get("gists_url"),
                        uj.get("starred_url"),uj.get("subscriptions_url"),uj.get("organizations_url"),
                        uj.get("repos_url"),uj.get("events_url"),uj.get("received_events_url"),uj.get("type"),
                        uj.get("site_admin"),uj.get("name"),uj.get("company"),uj.get("blog"),uj.get("location"),
                        uj.get("email"),uj.get("hireable"),uj.get("bio"),
                        uj.get("public_repos"),uj.get("public_gists"),uj.get("followers"),
                        uj.get("following"),uj.get("created_at"),uj.get("updated_at"))
            db.session.add(user)
            db.session.commit()

            if uj.get("id") == None:
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
