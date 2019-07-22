from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_cart_message(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented, but should be"

    def should_not_be_any_items_in_basket(self):
        self.is_not_element_present(*CartPageLocators.ITEMS_ADDED_TO_BASKET), \
            "At least one item is presented in the basket, but should not be"
