import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException,ElementNotSelectableException)

def test_explicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # driver.implicitly_wait(5)

    email_element = driver.find_element(By.XPATH,"//input[@id='login-username']")
    email_element.send_keys("abhijathar0709@gmail.com")
    password_element = driver.find_element(By.XPATH,"//input[@id='login-password']")
    password_element.send_keys("145733")
    submit_button_element = driver.find_element(By.XPATH,"//button[@id='js-login-btn']")
    submit_button_element.click()

    ignore_list = [ElementNotVisibleException,ElementNotSelectableException]

    # Fluent wait
    (WebDriverWait(driver=driver,poll_frequency=1,timeout=5,ignored_exceptions=ignore_list)
     .until(
        EC.visibility_of_element_located
        ((By.XPATH,"//div[@id='js-notification-box-msg']"))))

    notification_element = driver.find_element(By.XPATH,"//div[@id='js-notification-box-msg']")
    assert notification_element.text == "Your email, password, IP address or location did not match"

    driver.quit()


