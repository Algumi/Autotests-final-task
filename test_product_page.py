from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.click_on_add_to_basket_button()
    page.solve_quiz_and_get_code()

    page.check_messages_after_adding_to_basket()
    page.check_product_name_in_added_message(page.get_product_name_from_header())
    page.check_basket_total_in_basket_message(page.get_product_price_on_page())
