import pytest
from selenium import webdriver
from pages.favourites_page.favourites_page import FavouritesPage
from pages.product_list_page.product_list_page import ProductListPage
from pages.pruduct_page.product_page import ProductPage
from pages.sign_in_page.sign_in_page import SignInPage


@pytest.fixture(scope='function')
def browser():

    browser = webdriver.Chrome('../drivers/chromedriver')
    url_1 = 'https://prom.ua/Velosipednye-shiny'
    browser.get(url_1)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def sign_in(browser) -> SignInPage:
    yield SignInPage(browser)


@pytest.fixture
def product_list(browser) -> ProductListPage:
    yield ProductListPage(browser)


@pytest.fixture
def favourites(browser) -> FavouritesPage:
    yield FavouritesPage(browser)


@pytest.fixture
def product(browser) -> ProductPage:
    yield ProductPage(browser)
