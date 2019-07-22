from pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_to_basket_button()
    page.solve_quiz_and_get_code()

    page.check_messages_after_adding_to_basket()
    page.check_product_name_in_added_message(page.get_product_name_from_header())
    page.check_basket_total_in_basket_message(page.get_product_price_on_page())


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
