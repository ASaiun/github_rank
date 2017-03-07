import json

import requests
import time
from requests import ConnectionError

from sqlalchemy import desc
from crawler.base import Base
from config import Config
from model.userData import User
from model import session


class CrawlUser(Base):
    def __init__(self):
        self.username = Config.GITHUB_USER
        self.password = Config.GITHUB_PASSWORD
        self.base_url = Config.BASE_URL
        self.id = session.query(User.id).order_by(desc(User.id)).first()[0]

    def start(self):
        from_id = self.id
        flag = True
        while (flag):
            try:
                temp_id, count = self.parse(from_id)
                if temp_id == None:
                    flag = False
                if count == 100:
                    from_id = temp_id
            except ConnectionError:
                time.sleep(30)

    def crawl(self, from_id):
        url = self.base_url + '/users?since=' + str(from_id) + "&per_page=100"
        print(url)
        return requests.get(url, auth=(self.username, self.password))

    def parse(self, from_id):
        count = 0
        for uj in json.loads(self.crawl(from_id).text.encode('utf-8')):
            count = count + 1          
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
            temp_id = uj.get("id")

        return temp_id, count
