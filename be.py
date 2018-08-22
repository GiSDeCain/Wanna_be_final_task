from config import Config


class Backend:

    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        wd = self.app.wd
        wd.get(Config.apanel)

    def login(self):
        wd = self.app.wd
        wd.find_element_by_class_name("username").clear()
        wd.find_element_by_class_name("username").send_keys(Config.admin)
        wd.find_element_by_class_name("password").clear()
        wd.find_element_by_class_name("password").send_keys(Config.apasswd)
        wd.find_element_by_class_name("login").click()

    def open_catalog(self):
        wd = self.app.wd
        wd.find_element_by_class_name("Catalog").click()

    def select_category(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Konrad")

    def add_new_product(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="main"]/ul/li[2]/a').click()

    def fill_new_product(self):
        wd = self.app.wd
        wd.find_element_by_class_name("name[en]").clear()
        wd.find_element_by_class_name("name[en]").send_keys(Config.product_name01)


__author__ = 'GiSDeCain'
