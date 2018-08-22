

def test_add_product(app):
    app.backend.open_main_page()
    app.backend.login()
    app.backend.open_catalog()
    app.backend.select_category()
    app.backend.add_new_product()
    assert app.backend.newly_created_product() == app.Config.product_name01
    app.frontend.open_main_page()
    app.frontend.go_to_category()


__author__ = 'GiSDeCain'
