

class Frontend:

    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        wd = self.app.wd
        wd.get(Config.shop)


__author__ = 'GiSDeCain'
