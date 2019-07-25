from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
import pytest
import time


@pytest.mark.registered_user
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        test_email = str(time.time()) + "@fakemail.org"
        test_password = "test12345_TEST"
        page = LoginPage(browser, link)
        page.open()
        self.browser = browser
        page.register_new_user(test_email, test_password)
        page.should_be_authorized_user()
        time.sleep(10)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.click_on_add_to_basket_button()
        page.solve_quiz_and_get_code()

        page.check_messages_after_adding_to_basket()
        page.check_product_name_in_added_message(page.get_product_name_from_header())
        page.check_basket_total_in_basket_message(page.get_product_price_on_page())


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.check_messages_after_adding_to_basket()
    page.check_product_name_in_added_message(page.get_product_name_from_header())
    page.check_basket_total_in_basket_message(page.get_product_price_on_page())


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = CartPage(browser, browser.current_url)
    page.should_not_be_any_items_in_basket()
    page.should_be_empty_cart_message()
