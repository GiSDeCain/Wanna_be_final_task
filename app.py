import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from be import Backend
from fe import Frontend


@pytest.fixture
def app(request):
    fixture = Application
    request.addfinalizer(fixture.destroy)
    return fixture


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
