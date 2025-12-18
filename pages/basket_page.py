from .base_page import BasePage
from .locators import BasketLocators



class BasketPage(BasePage):

    def basket_not_empty(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_NOT_EMPTY), "Корзина не пуста"
        print(self.browser.find_element(*BasketLocators.EMPTY_BASKET).text)

    def basket_empty(self):
        assert self.is_element_present(*BasketLocators.EMPTY_BASKET), "Корзина пуста"
        print(self.browser.find_element(*BasketLocators.EMPTY_BASKET).text)
