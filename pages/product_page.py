from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage): 
    def should_be_basket_button(self):
        assert self.is_element_present(*BasketPageLocators.ADD_2_BASKET), "Basket button is not here"

    def basket_button_click(self):
        basket_button = self.browser.find_element(*BasketPageLocators.ADD_2_BASKET)
        basket_button.click()
        #BasePage.solve_quiz_and_get_code(self) Часть с кодом дял решения уровнений в попапе, которая сейчас не нужна.
    
    def true_name(self):
        true_name = self.browser.find_element(*BasketPageLocators.BOOK_TRUE_NAME)
        print(true_name.text)
        ttrue_name = true_name.text
        book_name = self.browser.find_element(*BasketPageLocators.BOOK_NAME)
        print(book_name.text)
        bbook_name = book_name.text

        assert ttrue_name == bbook_name, "Значения разные"

    def book_price(self):
        book_price = self.browser.find_element(*BasketPageLocators.BOOK_PRICE)
        print(book_price.text)
    
    def no_msg(self):
        assert self.is_not_element_present(*BasketPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        print(self.browser.find_element(*BasketPageLocators.SUCCESS_MESSAGE).text)

    def msg_gone(self):
        assert self.is_disappeared(*BasketPageLocators.SUCCESS_MESSAGE), "Success message has not disappeared, but should not be"