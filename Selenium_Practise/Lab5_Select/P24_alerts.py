# Alerts
#
# 1. Normal JS Alert
# 2. Confirm
# 3. Prompts
# 4. Native Alerts( Which we can't handle) - Selenium - pywinauto... sikuli( ui Desktop Automation)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_JS_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    button_1 = driver.find_element(By.CSS_SELECTOR,"button[onclick='jsAlert()']")
    button_1.click()
    WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    result1 = driver.find_element(By.ID,"result")
    print(result1.text)
    assert result1.text == "You successfully clicked an alert"

    # time.sleep(3)

def test_js_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    button2 = driver.find_element(By.CSS_SELECTOR,"button[onclick='jsConfirm()']")
    button2.click()
    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()
    result1 = driver.find_element(By.ID,"result")
    print(result1.text)
    assert result1.text == "You clicked: Ok"
    time.sleep(3)
    button2 = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
    button2.click()
    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss()
    result1 = driver.find_element(By.ID, "result")
    print(result1.text)
    assert result1.text == "You clicked: Cancel"

def test_js_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    button2 = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
    button2.click()
    WebDriverWait(driver=driver, timeout=3).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Abhijeet Jathar")
    alert.accept()
    result1 = driver.find_element(By.ID, "result")
    print(result1.text)
    assert result1.text == "You entered: Abhijeet Jathar"

