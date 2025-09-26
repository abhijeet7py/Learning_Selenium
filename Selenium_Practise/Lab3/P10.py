from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pytest
import allure
@pytest.mark.negative
@allure.title("Test Negative login 1")
def testP10_1():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    username = driver.find_element(By.ID,"username")
    username.send_keys("stud")
    password = driver.find_element(By.ID,"password")
    password.send_keys("Password123")
    login = driver.find_element(By.XPATH,"//button[@id='submit']")
    login.click()

    error = driver.find_element(By.ID,"error")
    print(error.text)

    assert error.text == "Your username is invalid!"

@pytest.mark.negative
@allure.title("Test Negative login 2")
def testP10_2():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    username = driver.find_element(By.ID, "username")
    username.send_keys("student")
    password = driver.find_element(By.ID, "password")
    password.send_keys("Password1")
    login = driver.find_element(By.XPATH, "//button[@id='submit']")
    login.click()
    time.sleep(5)
    error = driver.find_element(By.ID, "error")
    print(error.text)

    assert error.text == "Your password is invalid!"