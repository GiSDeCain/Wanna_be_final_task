from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.be import Backend
from Pages.fe import Frontend


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(2)
        self.backend = Backend(self)
        self.frontend = Frontend(self)

    def destroy(self):
        self.wd.close()
        self.wd.quit()


__author__ = 'GiSDeCain'
