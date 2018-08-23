from config import Config


def test_add_product(app):
    # app.backend.open_login_page()
    # app.backend.login()
    # app.backend.open_catalog()
    # app.backend.select_category()
    # app.backend.add_new_product()
    # app.backend.fill_new_product()
    # assert Config.product_name01  == app.backend.newly_created_product()
    app.frontend.open_main_page()
    app.frontend.go_to_category()
    assert Config.product_name01 == app.frontend.find_added_product()
    assert app.frontend.find_label_new() == "NEW"
    app.frontend.open_added_product()
    app.frontend.add_product_to_cart()
    app.frontend.close_product_window()
    app.frontend.open_cart()
    assert Config.product_name01 == app.frontend.find_product_name_in_cart()


__author__ = 'GiSDeCain'
