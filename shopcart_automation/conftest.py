import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utilities.read_config import ReadConfig

@pytest.fixture
def setup():
    browser = ReadConfig.get_browser()

    print(browser,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

    if browser == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()