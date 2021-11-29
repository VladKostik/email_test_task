from selenium.webdriver.android.webdriver import WebDriver
from pages.basepage import BasePage
from pages.pruduct_page.product_loators_collection import ProductLocatorsCollection


class ProductPage(BasePage):
    def __init__(self, browser: WebDriver):
        super().__init__(browser)
        self.__locator_collection = ProductLocatorsCollection()

    def find_add_to_favourites_button(self) -> None:
        # self._wait_for_element_located_and_visible(self.__locator_collection.add_to_favourites_button)
        self._wait_for_element_located_and_visible(self.__locator_collection.add_to_favourites_button)
