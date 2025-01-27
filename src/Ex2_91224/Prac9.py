import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_insta_login():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")

    username_element = driver.find_element(By.XPATH,"//input[@class = '_aa4b _add6 _ac4d _ap35']")
    username_element.send_keys("")
    password_element = driver.find_element(By.XPATH,"//input[@name = 'password']")
    password_element.send_keys("")
    login_element = driver.find_element(By.XPATH,"//button[@type = 'submit']")
    login_element.click()
