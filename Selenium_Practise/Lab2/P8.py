from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def testP8():
    # create instance of chrome driver class
    driver = webdriver.Chrome()
    # Navigate to the URL
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # find the element
    appointment_btn =  driver.find_element(By.ID,"btn-make-appointment")
    # appointment_btn =  driver.find_element(By.CLASS_NAME,"btn")
    appointment_btn.click()

    # verify the url
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(5)

    # Find the username & password and click on login
    username = driver.find_element(By.XPATH,"//input[@id='txt-username']")
    username.send_keys("John Doe")
    password =  driver.find_element(By.ID,"txt-password")
    password.send_keys("ThisIsNotAPassword")
    login = driver.find_element(By.ID,"btn-login")
    login.click()
# "https://katalon-demo-cura.herokuapp.com/#appointment"
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    time.sleep(10)
