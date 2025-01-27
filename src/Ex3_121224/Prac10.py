import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_neg():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/profile.php#login")
    usr_element = driver.find_element(By.ID,"txt-username")
    usr_element.send_keys("sdvds")
    pwd_element = driver.find_element(By.ID,"txt-password")
    pwd_element.send_keys("6623")
    log_element = driver.find_element(By.ID,"btn-login")
    log_element.click()
    time.sleep(5)

    noti_element = driver.find_element(By.XPATH,"//p[@class='lead text-danger']")
    # assert noti_element.text == "Login failed! Please ensure the username and password are valid."
    time.sleep(5)