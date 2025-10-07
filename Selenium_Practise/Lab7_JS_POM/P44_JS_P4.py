from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_JS_P4():
    driver = webdriver.Chrome()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()

    # Scroll to div
    username_div = driver.find_element(By.XPATH,"//div[@id='userName']")
    driver.execute_script("arguments[0].scrollIntoView(true);", username_div)
    time.sleep(2)

    # Step 1: Get shadow host (div#userName)
    shadow_host = driver.find_element(By.CSS_SELECTOR, "div#userName")
    time.sleep(2)

    # Step 2: Get shadow root from host
    shadow_root_1 = driver.execute_script("return arguments[0].shadowRoot", shadow_host)

    # Step 3: Find element inside shadow root (#kils)
    username = shadow_root_1.find_element(By.CSS_SELECTOR, "#kils")
    username.send_keys("Abhijeet Jathar")

    shadow_host_2 = shadow_root_1.find_element(By.CSS_SELECTOR, "div#app2")
    time.sleep(2)
    shadow_root_2 = driver.execute_script("return arguments[0].shadowRoot", shadow_host_2)
    pizza = shadow_root_2.find_element(By.CSS_SELECTOR, "#pizza")
    pizza.send_keys("Pasta")

    time.sleep(5)
    driver.quit()
