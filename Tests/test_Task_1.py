

def test_add_product(app):
    app.backend.open_login_page()
    app.backend.login()
    app.backend.open_catalog()
    app.backend.select_category()
    app.backend.add_new_product()


__author__ = 'GiSDeCain'
