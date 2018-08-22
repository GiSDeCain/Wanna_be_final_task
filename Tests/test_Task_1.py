from be import *


def test_add_product(Common, Backend):
    Common.open_login_page_be()
    Backend.login_be()
    Backend.open_catalog()


__author__ = 'GiSDeCain'
