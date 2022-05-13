import pytest
from .pages.product_page import ProductPage
from .pages.locators import PromoPageLocators


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
