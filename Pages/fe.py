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

    def find_added_product(self):
        wd = self.app.wd
        element = wd.find_element_by_class_name(Config.product_name01).text()
        return element

    def find_label_new(self):
        wd = self.app.wd
        element = wd.find_element_by_class_name("sticker new").text()
        return element


__author__ = 'GiSDeCain'
