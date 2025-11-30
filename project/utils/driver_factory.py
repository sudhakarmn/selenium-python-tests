from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class DriverFactory:

    @staticmethod
    def create_driver():
        driver = webdriver.Chrome()
        return driver
