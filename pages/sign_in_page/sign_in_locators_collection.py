from selenium.webdriver.common.by import By
from pages.core.locator import Locator


class SignInLocatorsCollection:
    def __init__(self):
        self.__sign_in_button = Locator(By.XPATH, '//div/button[@data-qaid="sign-in"]')
        self.__email_button = Locator(By.XPATH, '//div[@data-qaid="email_btn"]')
        self.__email_field = Locator(By.XPATH, '//div/input[@id="email_field"]')
        self.__password_field = Locator(By.XPATH, '//div/input[@id="enterPassword"]')
        self.__confirm_button = Locator(By.XPATH, '//div/button[@id="enterPasswordConfirmButton"]')

    @property
    def sign_in_button(self):
        return self.__sign_in_button

    @property
    def email_button(self):
        return self.__email_button

    @property
    def email_field(self):
        return self.__email_field

    @property
    def password_field(self):
        return self.__password_field

    @property
    def confirm_button(self):
        return self.__confirm_button
