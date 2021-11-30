import time
from selenium.common.exceptions import NoSuchElementException


def test_product_list_page_for_heart_pictogram_1(product_list, browser):
    """Verify that add-to-favourite buttons are present on product list page"""
    # Make sure that element is present on the DOM of a page and visible
    try:
        product_list.find_add_to_favourite_btn_to_check_presence()

    except NoSuchElementException:
        print(f'\nDefect found on page {browser.current_url}')
        time.sleep(2)
        browser.save_screenshot('../tests/screenshots/scr_1.png')
        raise Exception('No element on page')


def test_product_page_for_heart_pictogram_2(sign_in, product_list, product, browser):
    """Verify that add-to-favourite button is present on product page"""
    # Sign in via e-mail
    sign_in.sign_in()
    # Click on product block
    product_list.click_product()
    # Make sure that element is present on the DOM of a page and visible
    try:
        product.find_add_to_favourites_button()
    except NoSuchElementException:
        print(f'\nDefect found on page {browser.current_url}')
        time.sleep(2)
        browser.save_screenshot('../tests/screenshots/scr_2.png')
        raise Exception('No element on page')


def test_favourites_counter_presence_3(sign_in, product_list, browser, favourites):
    """Verify that favourite products counter is empty/or lacks on Favourites Page"""

    # Sign in via e-mail
    sign_in.sign_in()
    # Click on the add-to-favourite element and make it active
    product_list.click_add_to_favourite_btn()
    # Click on the same add-to-favourite element and make it inactive
    product_list.click_add_to_favourite_btn()
    # Click on favourites counter - navigate to the User`s Favourites Page
    product_list.click_favourites_counter()
    time.sleep(2)
    # Find counter element and if it has found get it`s content
    try:
        counter_element = favourites.find_favourites_counter()
        counter_value = counter_element.get_attribute('innerHTML')
        # Make sure that element`s content is not empty
        assert counter_value == ''
    except NoSuchElementException:
        pass
    except AssertionError:
        print(f'\nDefect found on page {browser.current_url}')
        time.sleep(2)
        browser.save_screenshot('../tests/screenshots/scr_3.png')
        raise AssertionError


def test_favourites_counter_value_4(sign_in, product_list, browser, favourites):
    """Verify that favourite products counter value on the Favourites Page corresponds to the number
    of products actually added to favourites

    """
    # Sign in via e-mail
    sign_in.sign_in()
    # Click on the add-to-favourite element
    product_list.click_add_to_favourite_btn()
    time.sleep(2)
    # Click on favourites counter - navigate to the User`s Favourites Page
    product_list.click_favourites_counter()
    # Save counter element
    counter_element = favourites.find_favourites_counter()
    # Get text from counter element div
    counter_value = counter_element.get_attribute('innerHTML')
    # Compare number of products added to favourites (one) with displayed counter value
    try:
        assert counter_value == '1'
    except AssertionError:
        print(f'\nDefect found on page {browser.current_url}')
        time.sleep(2)
        browser.save_screenshot('../tests/screenshots/scr_4.png')
        raise AssertionError


def test_add_to_favourites_element_changes_5(sign_in, product_list, browser):
    """Verify that element becomes different after clicking"""

    # Sign in via e-mail
    sign_in.sign_in()
    # Save element`s attributes before the click
    element_before_click = product_list.find_add_to_favourite_element_to_compare()
    element_before_click_attr = element_before_click.get_attribute('data-tg-clicked')
    # Click on the element
    product_list.click_add_to_favourite_btn()
    # Save element`s attributes after the click
    element_after_click = product_list.find_add_to_favourite_element_to_compare()
    element_after_click_attr = element_after_click.get_attribute('data-tg-clicked')

    try:
        assert element_before_click_attr != element_after_click_attr
    except AssertionError:
        print(f'\nDefect found on page {browser.current_url}')
        time.sleep(2)
        browser.save_screenshot('../tests/screenshots/scr_5.png')
        raise Exception('Element doesn`t change attributes')
