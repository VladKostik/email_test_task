from selenium.webdriver.common.by import By

from pages.core.locator import Locator


class ProductListLocatorCollection:
    def __init__(self):
        self.__add_to_favourite_element_path_css = (
            '#page-block > div > div._3L2HZ > div:nth-child(4) > '
            'div._1KcTA._2q9cL > div > div.yJNOx._28Dd5 > '
            'div._1KcTA._2gVBb.ZNadD._1aUF2._2P48h > div:nth-child(1) > '
            'div > div:nth-child(2) > div > div:nth-child(6) > div > '
            'div:nth-child(2) > span > svg > path'
        )
        self.__add_to_favourite_element_btn_css = Locator(
            By.CSS_SELECTOR,
            '#page-block > div > div._3L2HZ > div:nth-child(4) > '
            'div._1KcTA._2q9cL > div > div.yJNOx._28Dd5 > '
            'div._1KcTA._2gVBb.ZNadD._1aUF2._2P48h > div:nth-child(1) > '
            'div > div:nth-child(3) > div > div:nth-child(6) > div > div:nth-child(2) > span'
        )
        self.__add_to_favourite_button = Locator(By.XPATH, '//div/span[@data-qaid="add_favorite"][1]')
        self.__favourites_counter = Locator(
            By.CSS_SELECTOR,
            '#page-block > div > header > div > div > div > div > '
            'div:nth-child(3) > div > div:nth-child(1) > button > svg'
        )
        self.__product_selector = Locator(
            By.CSS_SELECTOR,
            '#page-block > div > div._3L2HZ > div:nth-child(4) > '
            'div._1KcTA._2q9cL > div > div.yJNOx._28Dd5 > '
            'div._1KcTA._2gVBb.ZNadD._1aUF2._2P48h > div:nth-child(1) > '
            'div > div:nth-child(5) > div > a'
        )

    @property
    def add_to_favourite_element_path_css(self):
        return self.__add_to_favourite_element_path_css

    @property
    def add_to_favourite_element_btn_css(self):
        return self.__add_to_favourite_element_btn_css

    @property
    def add_to_favourite_btn(self):
        return self.__add_to_favourite_button

    @property
    def favourites_counter(self):
        return self.__favourites_counter

    @property
    def product_selector(self):
        return self.__product_selector
