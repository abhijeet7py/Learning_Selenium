from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def testP9():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    username = driver.find_element(By.ID,"login-username")
    username.send_keys("abhi@gail.com")
    password = driver.find_element(By.ID,"login-password")
    password.send_keys("123456")
    login = driver.find_element(By.XPATH,"//button[@id='js-login-btn']")
    login.click()