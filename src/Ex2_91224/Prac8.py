import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_prac8():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    username_element = driver.find_element(By.XPATH,"//input[@id = 'txt-username']")
    username_element.send_keys("John Doe")
    password_element = driver.find_element(By.XPATH,"//input[@id = 'txt-password']")
    password_element.send_keys("ThisIsNotAPassword")

    login_element = driver.find_element(By.ID,"btn-login")
    login_element.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(5)