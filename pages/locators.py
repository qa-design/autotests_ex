from selenium.webdriver.common.by import By
import pytest


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-group>a')

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    URL = 'http://selenium1py.pythonanywhere.com/basket/'
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
    BASKET_ITEM_IS_ADDED = (By.CSS_SELECTOR, '.basket-title>.row>h2')


class MainPageLocators:
    URL = 'http://selenium1py.pythonanywhere.com/'


class LoginPageLocators():
    URL = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name=registration_submit]')


class ProductPageLocators:
    URL = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'


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
    URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    NAME_ADDED_ITEM_TO_BASKET = (By.CSS_SELECTOR, '.alertinner>strong')
    CORRECT_NAME_ITEM = (By.CSS_SELECTOR, '.product_main>h1')
    ADDED_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    CORRECT_PRICE = (By.CSS_SELECTOR, '.product_main>p.price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')
