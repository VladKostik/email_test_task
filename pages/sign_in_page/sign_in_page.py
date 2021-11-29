from selenium.webdriver.chrome.webdriver import WebDriver
from pages.core.get_sign_in_data import email, password
from pages.basepage import BasePage
from pages.sign_in_page.sign_in_locators_collection import SignInLocatorsCollection


class SignInPage(BasePage):
    def __init__(self, browser: WebDriver):
        super().__init__(browser)
        self.__locators_collection = SignInLocatorsCollection()

    def sign_in(self) -> None:
        self._click(self.__locators_collection.sign_in_button)
        self._click(self.__locators_collection.email_button)
        self._send_keys(self.__locators_collection.email_field, email)
        self._send_keys(self.__locators_collection.password_field, password)
        self._click(self.__locators_collection.confirm_button)
