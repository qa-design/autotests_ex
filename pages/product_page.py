from .base_page import BasePage
from .locators import PromoPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*PromoPageLocators.ADD_TO_CART_BTN).click()
        self.solve_quiz_and_get_code()

    def check_name_item_added_to_basket(self):
        assert self.browser.find_element(*PromoPageLocators.NAME_ADDED_ITEM_TO_BASKET).text == \
               self.browser.find_element(*PromoPageLocators.CORRECT_NAME_ITEM).text, 'Name of added item is ' \
                                                                                             'incorrect '

    def check_price_item_added_to_basket(self):
        assert self.browser.find_element(*PromoPageLocators.ADDED_PRICE).text == \
               self.browser.find_element(*PromoPageLocators.CORRECT_PRICE).text, 'Price of added item is incorrect'
