

def test_add_product(app):
    app.Backend.open_login_page()
    app.Backend.login()
    app.Backend.open_catalog()
    app.Backend.select_category()
    app.Backend.add_new_product()


__author__ = 'GiSDeCain'
