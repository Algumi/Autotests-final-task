from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        self.enter_email_for_registration(email)
        self.enter_password1_for_registration(password)
        self.enter_password2_for_registration(password)
        self.click_on_register_button()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def enter_email_for_registration(self, email):
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_INPUT).send_keys(email)

    def enter_password1_for_registration(self, password):
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_INPUT_1).send_keys(password)

    def enter_password2_for_registration(self, password):
        self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_INPUT_2).send_keys(password)

    def click_on_register_button(self):
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
