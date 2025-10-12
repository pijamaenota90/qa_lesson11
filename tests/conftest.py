import pytest
from selenium import webdriver
from selene import Browser, Config
from utils import attach


@pytest.fixture(scope='function')
def browser_setup():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        },
        "goog:chromeOptions": {
            "args": [
                "--no-user-data-dir",
                "--incognito",
                "--disable-dev-shm-usage",
                "--no-sandbox",
                "--disable-gpu"
            ]
        }
    }

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities
    )

    browser = Browser(Config(driver))

    try:
        yield browser
    finally:
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)
        attach.add_video(browser)
        browser.quit()