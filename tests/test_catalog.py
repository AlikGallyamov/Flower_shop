import pytest

from flower_shop_test.models.catalog import catalog
from flower_shop_test.pages.base_page import BasePage


def test_open_catalog(browser_managment):
    main_page = BasePage()
    main_page.open_url()
    main_page.open_catalog(catalog)