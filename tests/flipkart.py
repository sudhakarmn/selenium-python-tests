from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def flipkart():
    try:
        driver.get('https://www.flipkart.com/')
        search = driver.find_element(By.XPATH,"//input[@class='Pke_EE']")
        search.send_keys('iphone')
    except:
        print("error")
    finally:
        print("completed")
    
def test_dropdown_items():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Step 1: Open page
        driver.get('https://practicetestautomation.com/practice-test-table/')

        # Step 2: Click dropdown
        dropdown_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'dropdown-button'))
        )
        dropdown_btn.click()

        # Step 3: Get dropdown UL element
        dropdown_menu = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'dropdown-menu'))
        )

        # Step 4: Get all LI items
        items = dropdown_menu.find_elements(By.TAG_NAME, 'li')

        # Assertion 1: List should not be empty
        assert len(items) > 0, "Dropdown items list is EMPTY!"

        # Print all dropdown text
        print("Dropdown Options:")
        actual_items = []
        for item in items:
            text = item.text.strip()
            if text:
                actual_items.append(text)
                print(text)

        # Assertion 2: Validate expected values (customize based on site)
        expected_items = ['5,000+', '10,000+', '50,000+']  # sample values

        # Only check expected if they actually exist on UI
        for expected in expected_items:
            assert expected in actual_items, f"Expected item '{expected}' NOT FOUND in dropdown!"

        print("✔ Test Passed: All dropdown validations successful")

    except Exception as e:
        print("❌ Test Failed:", str(e))

    finally:
        driver.quit()

