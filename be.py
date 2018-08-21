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


__author__ = 'GiSDeCain'
