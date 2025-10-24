import pytest
from selenium import webdriver
from selene import browser
from utils import attach


@pytest.fixture(scope='function')
def browser_setup():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        },
        "goog:chromeOptions": {
            "args": [
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--headless=new"
            ]
        }
    }

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities
    )

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height=1080

    try:
        yield browser
    finally:
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)
        attach.add_video(browser)
        browser.quit()