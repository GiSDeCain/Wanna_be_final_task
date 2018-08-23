from config import Config


class Frontend:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        wd = self.app.wd
        wd.get(Config.shop)

    def go_to_category(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="box-category-tree"]/ul/li[1]/a').click()

    def open_added_product(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="box-category"]/div[2]/div[2]').click()

    def find_added_product(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath('//*[@id="box-category"]/div[2]/div[2]/div/a/div[2]').text
        return element

    def find_label_new(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath('//*[@id="box-category"]/div[2]/div[2]/div/a/div[1]/div').text
        return element

    def add_product_to_cart(self):
        wd = self.app.wd
        wd.find_element_by_name("add_cart_product").click()

    def close_product_window(self):
        wd = self.app.wd
        wd.find_element_by_xpath('/html/body/div[2]/div/div[1]').click()

    def open_cart(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="cart"]/a/div/div').click()

    def find_product_name_in_cart(self):
        wd = self.app.wd
        element = wd.find_element_by_xpath('//*[@id="box-checkout-cart"]/div/table/tbody/tr/td[2]/div/strong/a').text
        return element


__author__ = 'GiSDeCain'
