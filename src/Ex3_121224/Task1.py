from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def test_form():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    first_name_element = driver.find_element(By.XPATH,"//input[@name = 'firstname']")
    first_name_element.send_keys("Abhijeet")
    last_name_element = driver .find_element(By.XPATH,"//input[@placeholder = 'Last Name']")
    last_name_element.send_keys("Jathar")
    email_element = driver.find_element(By.XPATH,"//input[@id = 'input-email']")
    email_element.send_keys("abhijeet1243@gmail.com")
    telephone_element = driver.find_element(By.XPATH,"//input[@name = 'telephone']")
    telephone_element.send_keys("124567890")
    password_element = driver.find_element(By.XPATH,"//input[@name = 'password']")
    password_element.send_keys("Abc@1234")
    confirm_pass_element = driver.find_element(By.XPATH,"//input[@id = 'input-confirm']")
    confirm_pass_element.send_keys("Abc@1234")
    checkbox_element =  driver.find_element(By.XPATH,"//input[@name = 'agree']")
    checkbox_element.click()
    submit_element = driver.find_element(By.XPATH,"//input[@value= 'Continue']")
    submit_element.click()
    assert driver.current_url == "https://awesomeqa.com/ui/index.php?route=account/success"
    account_success_element = driver.find_element(By.XPATH,"//h1[text()='Your Account Has Been Created!']")
    assert account_success_element.text == "Your Account Has Been Created!"

    time.sleep(5)

# test_form()