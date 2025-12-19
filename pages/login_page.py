import time
from selenium import webdriver
from .base_page import BasePage
from .locators import LoginPageLocators

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Correct url is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(str(time.time()) + "@fakemail.org")
        password = str(time.time())
        password2 = password
        reg_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        reg_email.send_keys(email)
        reg_password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        reg_password.send_keys(password)
        reg_password_rep = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_REP)
        reg_password_rep.send_keys(password2)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
