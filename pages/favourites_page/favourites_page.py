from pages.basepage import BasePage
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from pages.favourites_page.favourites_locators_collection import FavouritesLocatorsCollection


class FavouritesPage(BasePage):
    def __init__(self, browser: WebDriver):
        super().__init__(browser)
        self.__locators_collection = FavouritesLocatorsCollection()

    def find_favourites_counter(self) -> WebElement:
        return self._browser.find_element_by_css_selector(self.__locators_collection.favourites_counter_at_fp)
