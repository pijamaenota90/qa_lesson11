
from selene import browser
import pytest

@pytest.fixture(scope='function', autouse=True)
def browser_setup():

    browser.config.driver_name = "chrome"
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    if browser.driver:
        browser.quit()
