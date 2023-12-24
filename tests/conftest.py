import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from flower_shop_test.controls import attach


@pytest.fixture()
def browser_managment():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)
    browser.config.driver = driver
    browser.config.base_url = 'https://azalianow.ru'
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.window_width = '1900'
    browser.config.window_height = '960'

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
