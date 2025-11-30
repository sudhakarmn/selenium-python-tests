from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
try:
    driver.get("https://practicetestautomation.com/practice-test-login/")
    username = driver.find_element(By.XPATH,'//input[@id="username"]')
    username.send_keys('student')
    driver.find_element(By.NAME,'password').send_keys('Password123')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button#submit"))
    )
    driver.find_element(By.CSS_SELECTOR,'button#submit').click()
    time.sleep(3)
    assert driver.current_url == 'https://practicetestautomation.com/logged-in-successfully/', 'URL mismatched'
    assert "Logged In Successfully" in driver.page_source
except Exception as e:
    print("Exception occured",e)
