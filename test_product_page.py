import time

import pytest
from .pages.product_page import ProductPage
from .pages.locators import PromoPageLocators
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PromoPageLocators.URL)
    page.open()
    page.add_to_basket()


@pytest.mark.parametrize('link', PromoPageLocators.COLLECT_PROMO_URL)
def test_guest_check_added_item(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_name_item_added_to_basket()


@pytest.mark.xfail(reason="this is correct")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PromoPageLocators.URL)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PromoPageLocators.URL)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="this is correct")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PromoPageLocators.URL)
    page.open()
    page.add_to_basket()
    page.should_disappear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.URL)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PromoPageLocators.URL)
    page.open()
    page.go_to_login_page()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, ProductPageLocators.URL)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
    basket_page.basket_should_be_empty()
