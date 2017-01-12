import os


class Config:

    SQLALCHECHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/github_rank"

    GITHUB_USER = os.environ.get('GITHUB_USER')
    GITHUB_PASSWORD = os.environ.get('GITHUB_PASSWORD')


