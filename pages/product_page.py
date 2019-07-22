from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_on_add_to_basket_button(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        login_link.click()
        return True

    def check_messages_after_adding_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
            'There is no "product has been added to basket" message'
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), \
            "There is no message about basket total sum"

    def check_product_name_in_added_message(self, product_name):
        assert self.get_product_name_from_message() == product_name, \
            "Product name from message doesn't match expected"

    def check_basket_total_in_basket_message(self, product_price):
        assert self.get_product_sum_from_message() == product_price, \
            "Basket total sum doesn't match expected"

    def get_product_name_from_message(self):
        return self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text

    def get_product_name_from_header(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_sum_from_message(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_SUM).text

    def get_product_price_on_page(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_TO_BASKET_MESSAGE), \
            "Success message is presented, but should not be"
