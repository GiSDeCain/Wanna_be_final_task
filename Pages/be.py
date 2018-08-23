from config import Config


class Backend:

    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        wd = self.app.wd
        wd.get(Config.apanel)

    def login(self):
        wd = self.app.wd
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(Config.admin)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(Config.apasswd)
        wd.find_element_by_xpath('//*[@id="box-login"]/form/div[2]/button').click()

    def open_catalog(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="app-"][2]').click()

    def select_category(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Konrad").click()

    def add_new_product(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="main"]/ul/li[2]/a').click()

    def fill_new_product(self):
        wd = self.app.wd
        wd.find_element_by_class_name("name[en]").clear()
        wd.find_element_by_class_name("name[en]").send_keys(Config.product_name01)
        wd.find_element_by_xpath('//*[@id="tab-general"]/div/div[1]/div[1]/div/div/label[1]').click()
        wd.find_element_by_link_text("Price").click()
        wd.find_element_by_class_name("prices[USD]").clear()
        wd.find_element_by_class_name("prices[USD]").send_keys(Config.product_price)
        wd.find_element_by_class_name("save").click()

    def newly_created_product(self):
        wd = self.app.wd
        element = wd.find_element_link_text(Config.product_name01)
        return element


__author__ = 'GiSDeCain'
