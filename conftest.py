import pytest
from applocation import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


__author__ = 'GiSDeCain'