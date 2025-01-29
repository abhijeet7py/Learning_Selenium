from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import allure
import time

@pytest.mark.negative
@allure.title("Negative Testcase - App.vwo.com - Wrong Email, Pass -> Error Message.")
@allure.description("Verify that if email/pass is wrong, we will get a message")
def test_negative_vwo_login_project2():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email_element = driver.find_element(By.ID,"login-username")
    email_element.send_keys("abhijeetjathar0709@gmail.com")
    password_element = driver.find_element(By.NAME,"password")
    password_element.send_keys("123456789")
    signin_element = driver.find_element(By.ID,"js-login-btn")
    signin_element.click()
    time.sleep(3)
    notification_element = driver.find_element(By.CLASS_NAME,"notification-box-description")



    time.sleep(5)
    driver.quit()

# test_negative_vwo_login_project2()