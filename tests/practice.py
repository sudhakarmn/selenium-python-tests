from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('https://practicetestautomation.com/practice-test-table/')
    dropdown_button = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.CLASS_NAME,'dropdown-button'))
    )
    dropdown_button.click()
    dropdown_ul = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.CLASS_NAME,'dropdown-menu'))
    )

    dropdown_li = dropdown_ul.find_elements(By.TAG_NAME,'li')

    assert len(dropdown_li) > 0 , "Zero list found"

    for i in dropdown_li:
        print(i.text)

except Exception as e:
    print("aaaa",e)

main = driver.current_window_handle

all_window = driver.window_handle

for w in all_window:
    if w != main:
        driver.switch_to.widnow(w)