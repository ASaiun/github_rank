from crawler.crawlUser import CrawlUser
from model.userData import User
from model import session


class UserStore():

    def user_store(self):
        c = CrawlUser()
        count = 0
        from_id = 0

        flag = True
        while (flag):
            for uj in c.get_id_user_data(from_id):
                count = count + 1
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

                if uj.get("id") == None:
                    flag = False

                if count == 30:
                    count = 0
                    from_id = uj.get("id")