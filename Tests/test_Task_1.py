from config import Config

def test_add_product(app):
    app.backend.open_login_page()
    app.backend.login()
    app.backend.open_catalog()
    app.backend.select_category()
    app.backend.add_new_product()
    app.backend.fill_new_product()
    #assert app.backend.newly_created_product() == Config.product_name01
    app.frontend.open_main_page()
    app.frontend.go_to_category()
    #assert app.frontend.find_added_product() == Config.product_name01
    #assert app.frontend.find_label_new() == "New"
    app.frontend.open_added_product()
    app.frontend.add_product_to_cart()
    app.frontend.open_cart()
    #assert app.frontend.find_product_name_in_cart() == Config.product_name01


__author__ = 'GiSDeCain'
