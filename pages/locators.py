from selenium.webdriver.common.by import By
import pytest


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class PromoPageLocators:
    COLLECT_PROMO_URL = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                         pytest.param(
                             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                             marks=pytest.mark.xfail
                         ),
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
    URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    NAME_ADDED_ITEM_TO_BASKET = (By.CSS_SELECTOR, '.alertinner>strong')
    CORRECT_NAME_ITEM = (By.CSS_SELECTOR, '.product_main>h1')
    ADDED_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    CORRECT_PRICE = (By.CSS_SELECTOR, '.product_main>p.price_color')
