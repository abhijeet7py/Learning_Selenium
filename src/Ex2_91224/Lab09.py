from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_VWO_login():
    # 1. Open the URL
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    # 2. find and enter the details of username and password
    username_button = driver.find_element(By.ID,"login-username")
    username_button.send_keys("abhijeetjathar0709@gmail.com")
    password_button = driver.find_element(By.ID,"login-password")
    password_button.send_keys("1234567890")
    # 3. Find and click on login
    login_button = driver.find_element(By.ID,"js-login-btn")
    login_button.click()
    # 4. Verify the URL
    # assert
    time.sleep(5)
    driver.quit()

test_VWO_login()


