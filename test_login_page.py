from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators


def test_login_form(browser):
    page = LoginPage(browser, LoginPageLocators.URL)
    page.open()
    page.should_be_login_page()