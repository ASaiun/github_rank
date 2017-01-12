# from . import db
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#
#     id = db.Column(db.Integer, primary_key=True)
#     login = db.Column(db.String(64))
#     avatar_url = db.Column(db.String(128))
#     gravatar_id = db.Column(db.String(64))
#     url = db.Column(db.String(128))
#     html_url = db.Column(db.String(128))
#     followers_url = db.Column(db.String(128))
#     following_url = db.Column(db.String(128))
#     gists_url = db.Column(db.String(128))
#     starred_url = db.Column(db.String(128))
#     subscriptions_url = db.Column(db.String(128))
#     organizations_url = db.Column(db.String(128))
#     repos_url = db.Column(db.String(128))
#     events_url = db.Column(db.String(128))
#     received_events_url = db.Column(db.String(128))
#     type = db.Column(db.String(64))
#     site_admin = db.Column(db.Boolean)
#     name = db.Column(db.String(64))
#     company = db.Column(db.String(128))
#     blog = db.Column(db.String(128))
#     location = db.Column(db.String(128))
#     email = db.Column(db.String(128))
#     hireable = db.Column(db.Boolean)
#     bio = db.Column(db.String(128))
#     public_repos = db.Column(db.Integer)
#     public_gists = db.Column(db.Integer)
#     followers = db.Column(db.Integer)
#     following = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime())
#     updated_at = db.Column(db.DateTime())
#
#     def __init__(self, id, login, avatar_url, gravatar_id, url,
#                  html_url, followers_url, following_url, gists_url,
#                  starred_url, subscriptions_url, organizations_url,
#                  repos_url, events_url, received_events_url, type,
#                  site_admin, name=None, company=None, blog=None, location=None, email=None, hireable=None, bio=None,
#                  public_repos=None, public_gists=None, followers=None, following=None, created_at=None,
#                  updated_at=None):
#         self.id = id
#         self.login = login
#         self.avatar_url = avatar_url
#         self.gravatar_id = gravatar_id
#         self.url = url
#         self.html_url = html_url
#         self.followers_url = followers_url
#         self.following_url = following_url
#         self.gists_url = gists_url
#         self.starred_url = starred_url
#         self.starred_url = starred_url
#         self.subscriptions_url = subscriptions_url
#         self.organizations_url = organizations_url
#         self.repos_url = repos_url
#         self.events_url = events_url
#         self.received_events_url = received_events_url
#         self.type = type
#         self.site_admin = site_admin
#         self.name = name
#         self.company = company
#         self.blog = blog
#         self.location = location
#         self.email = email
#         self.hireable = hireable
#         self.bio = bio
#         self.public_repos = public_repos
#         self.public_gists = public_gists
#         self.followers = followers
#         self.following = following
#         self.created_at = created_at
#         self.updated_at = updated_at
#
#
#
#     def __repr__(self):
#         return '<Users %r>' % self.name
