from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from pages.basepage import BasePage
from pages.product_list_page.productlist_locator_collection import ProductListLocatorCollection


class ProductListPage(BasePage):
    def __init__(self, browser: WebDriver):
        super().__init__(browser)
        self.__locators_collection = ProductListLocatorCollection()

    def find_add_to_favourite_element_to_compare(self) -> WebElement:
        return self._browser.find_element_by_css_selector(self.__locators_collection.add_to_favourite_element_path_css)

    def find_add_to_favourite_btn_to_check_presence(self) -> None:
        self._wait_for_element_located_and_visible(self.__locators_collection.add_to_favourite_element_btn_css)

    def click_add_to_favourite_btn(self) -> None:
        self._click(self.__locators_collection.add_to_favourite_btn)

    def click_favourites_counter(self) -> None:
        self._click(self.__locators_collection.favourites_counter)

    def click_product(self)-> None:
        self._click(self.__locators_collection.product_selector)
