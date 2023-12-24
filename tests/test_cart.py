import pytest

from flower_shop_test.data.data import card
from flower_shop_test.pages.base_page import BasePage


def test_add_product(browser_managment):
    main_page = BasePage()
    main_page.open_url()
    main_page.add_product(card)


def test_delete_product(browser_managment):
    main_page = BasePage()
    main_page.open_url()
    main_page.add_product(card)
    main_page.delete_product()


def test_search_product(browser_managment):
    main_page = BasePage()
    main_page.open_url()
    main_page.search_product(card)
