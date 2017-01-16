from sqlalchemy import Column, Integer, String, Boolean, DateTime

from model import DBBase


class User(DBBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String(64))
    avatar_url = Column(String(128))
    gravatar_id = Column(String(64))
    url = Column(String(128))
    html_url = Column(String(128))
    followers_url = Column(String(128))
    following_url = Column(String(128))
    gists_url = Column(String(128))
    starred_url = Column(String(128))
    subscriptions_url = Column(String(128))
    organizations_url = Column(String(128))
    repos_url = Column(String(128))
    events_url = Column(String(128))
    received_events_url = Column(String(128))
    type = Column(String(64))
    site_admin = Column(Boolean)
    name = Column(String(64))
    company = Column(String(128))
    blog = Column(String(128))
    location = Column(String(128))
    email = Column(String(128))
    hireable = Column(Boolean)
    bio = Column(String(128))
    public_repos = Column(Integer)
    public_gists = Column(Integer)
    followers = Column(Integer)
    following = Column(Integer)
    created_at = Column(DateTime())
    updated_at = Column(DateTime())

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
