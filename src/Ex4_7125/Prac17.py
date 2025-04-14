from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_explicit_wait():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    email = driver.find_element(By.ID,"login-username")
    email.send_keys("abhijeet123@gmail.com")
    password = driver.find_element(By.ID,"login-password")
    password.send_keys("123")
    signin = driver.find_element(By.ID,"js-login-btn").click()
    # error = driver.find_element(By.ID, "js-notification-box-msg")
    error = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.ID, "js-notification-box-msg")))
    # error = driver.find_element(By.ID,"js-notification-box-msg").text
    assert error.text == "Your email, password, IP address or location did not match"

    driver.quit()

