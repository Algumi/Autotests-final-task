from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators(object):
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_TOTAL_SUM = (By.XPATH, '//div[@id = "messages"]//div[contains(., "Your basket total is now")]//strong')
    ADDED_PRODUCT_NAME = (By.XPATH, '//div[@id = "messages"]//div[contains(., "been added to your basket.")]//strong')
    BASKET_TOTAL_MESSAGE = (By.XPATH, '//div[@id = "messages"]'
                                      '//div[@class="alertinner " and contains(., "Your basket total is now")]')
    ADDED_TO_BASKET_MESSAGE = (By.XPATH, '//div[@id = "messages"]'
                                         '//div[@class="alertinner " and contains(., "been added to your basket.")]')
