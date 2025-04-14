import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)


def test_fluent_wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email = driver.find_element(By.ID, "login-username")
    email.send_keys("abhijeet123@gmail.com")
    password = driver.find_element(By.ID, "login-password")
    password.send_keys("123")
    signin = driver.find_element(By.ID, "js-login-btn").click()
    ignore = [ElementNotVisibleException,ElementNotSelectableException]

    error = (WebDriverWait(driver,5,poll_frequency=2,ignored_exceptions=ignore).
             until(EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))))


    time.sleep(5)

    assert error.text == "Your email, password, IP address or location did not match"