# Locators

# Preference rule

# ID --> Name --> class name --> link/Partial link text --> Css Selector --> Xpath

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import allure
@allure.title("Negative Test case")
@allure.description("Verify Negative test case on VWO.com")
def testP16():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/#/login")
    email = driver.find_element(By.ID,"login-username")
    email.send_keys("abc@gmail.com")
    password = driver.find_element(By.NAME,"password")
    password.send_keys("1234")
    sign_in = driver.find_element(By.ID,"js-login-btn")
    sign_in.click()
    time.sleep(3)
    error = driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error.text)
    assert error.text == "Your email, password, IP address or location did not match"