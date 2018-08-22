from selenium.webdriver.chrome.webdriver import WebDriver
from config import Config


class Common:

    def __init__(self):
        self.wd = WebDriver

    def open_login_page_be(self):
        wd = self.wd
        wd.get(Config.apanel)

    def open_login_page_fe(self):
        wd = self.wd
        wd.get(Config.shop)


class Backend:

    def __init__(self):
        self.wd = WebDriver

    def login_be(self):
        wd = self.wd
        wd.find_element_by_class_name("username").clear()
        wd.find_element_by_class_name("username").send_keys(Config.admin)
        wd.find_element_by_class_name("password").clear()
        wd.find_element_by_class_name("password").send_keys(Config.apasswd)
        wd.find_element_by_class_name("login").click()

    def open_catalog(self):
        wd = self.wd
        wd.find_element_by_class_name("Catalog").click()


__author__ = 'GiSDeCain'
