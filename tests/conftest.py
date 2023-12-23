import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser_managment():
    browser.config.base_url = 'https://azalianow.ru'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_width = '1900'
    browser.config.window_height = '960'


    yield

    browser.quit()


