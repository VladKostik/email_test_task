from selenium.webdriver.common.by import By

from pages.core.locator import Locator


class ProductLocatorsCollection:
    def __init__(self):
        self._add_to_favourites_button = Locator(
            By.CSS_SELECTOR,
            '#page-block > div > div._3L2HZ > '
            'div:nth-child(1) > div.ek-body__section > '
            'div > div.yJNOx._3G_KF > div._1KcTA._3oDcT._2D4Ee > '
            'div > div._1KcTA.XsctY > div > div:nth-child(2) > span > svg'
        )

    @property
    def add_to_favourites_button(self):
        return self._add_to_favourites_button
