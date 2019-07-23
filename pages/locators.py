from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//a[contains(@class, "btn") and contains(@href, "basket") and contains(., "basket")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators(object):
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//div[@id = "content_inner" and contains(., "Your basket is empty")]')
    ITEMS_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_REGISTER_INPUT = (By.XPATH, '//input[@type = "email" and @name = "registration-email"]')
    PASSWORD_REGISTER_INPUT_1 = (By.XPATH, '//input[@type = "password" and @name = "registration-password1"]')
    PASSWORD_REGISTER_INPUT_2 = (By.XPATH, '//input[@type = "password" and @name = "registration-password2"]')
    REGISTER_BUTTON = (By.XPATH, '//button[@name = "registration_submit"]')


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
