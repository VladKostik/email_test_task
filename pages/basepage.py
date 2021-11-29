from typing import Tuple
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.core.locator import Locator


class BasePage:
    def __init__(self, browser):
        self._browser = browser
        self.__browser_wait = WebDriverWait(self._browser, 10)
        self.__actions = ActionChains(self._browser)

    def _wait_until_element_clickable(
            self,
            locator: Locator
    ) -> WebElement:
        return self.__browser_wait.until(
            EC.element_to_be_clickable(locator.to_tuple())
        )

    def _wait_for_element_located_and_visible(
            self,
            locator: Locator
    ) -> WebElement:
        return self.__browser_wait.until(
            EC.visibility_of_element_located(locator.to_tuple())
        )

    def _click(self, locator: Locator) -> None:
        self._wait_until_element_clickable(locator).click()

    def _send_keys(self, locator: Locator, keys: str) -> None:
        self._wait_until_element_clickable(locator).send_keys(keys)

    def _move_to_element(self, locator: Tuple[By, str]) -> WebElement:
        return self.__actions.move_to_element(
            self.__browser_wait.until(EC.presence_of_element_located(locator))
        ).perform()
