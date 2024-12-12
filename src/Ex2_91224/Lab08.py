from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_login_Katalon():
    # 1. Open the URL
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # 2. Find and click on make appointment button
    make_appointment_button = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_button.click()
    # 3. Verify the URL
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    # 4. find and enter the details of username and password
    # < input
    # type = "text"
    # class ="form-control"
    # id="txt-username"
    # name="username"
    # placeholder="Username"
    # value="" autocomplete="off"
    # >
    username_button = driver.find_element(By.ID,"txt-username")
    username_button.click()
    username_button.send_keys("John Doe")
    password_button = driver.find_element(By.ID,"txt-password")
    password_button.click()
    password_button.send_keys("ThisIsNotAPassword")
    # 5. click on the submit button
    login_button = driver.find_element(By.ID,"btn-login")
    login_button.click()
    # 6. Verify the URL
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"


    time.sleep(10)

test_login_Katalon()