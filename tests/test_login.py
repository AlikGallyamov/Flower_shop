import pytest

from flower_shop_test.models.authorization import login_window
from flower_shop_test.pages.base_page import BasePage


def test_open_login_window(browser_managment):
    main_page = BasePage()
    main_page.open_url()
    main_page.open_login_window(login_window)
