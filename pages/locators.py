from selenium.webdriver.common.by import By

class BasketPageLocators():
    ADD_2_BASKET = (By.ID, "add_to_basket_form")
    BOOK_TRUE_NAME = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    BOOK_NAME = (By.CSS_SELECTOR,"div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)")
    BOOK_PRICE = (By.CSS_SELECTOR,"div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"div.alert:nth-child(1) > div:nth-child(2)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")