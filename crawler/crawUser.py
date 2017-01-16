import json

import requests

from config import Config


class CrawUser(Config):
    def __init__(self, Config):
        self.username = Config.GITHUB_USER
        self.password = Config.GITHUB_PASSWORD
        self.base_url = 'https://api.github.com'

    def get_user_data(self):
        response = requests.get(self.base_url + '/users',
                                auth=(self.username, self.password))

        print response.status_code
        # print response.headers
        # print json.loads(response.text)[0].get('id')
        # print config.Config.GITHUB_USER
        # print config.Config.GTIHUB_PASSWORD
        return json.loads(response.text)
        # def get_user_data(self):

    def get_id_user_data(self, id=0):
        url = self.base_url + '/users?since=' + str(id)
        print url
        response = requests.get(url, auth=(self.username, self.password))
        print response.status_code
        print response.headers
        print json.loads(response.text)[0].get('id')

        return json.loads(response.text)

    def get_all_user_data(self):
        pass
        # for id_next in self.get_all_user_data()[id]
