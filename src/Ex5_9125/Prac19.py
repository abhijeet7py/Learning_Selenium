import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_JS_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    js_alert = driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    js_alert.click()

    WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    result = driver.find_element(By.ID,"result")
    assert result.text == "You successfully clicked an alert"

    time.sleep(5)

def test_JS_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    js_confirm = driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
    js_confirm.click()
    WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    # alert.accept()
    alert.dismiss()

    result = driver.find_element(By.ID,"result")
    # assert result.text == "You clicked: Ok"
    assert result.text == "You clicked: Cancel"

    time.sleep(5)

def test_JS_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    prompt = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    prompt.click()
    WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.send_keys("Abhijeet")
    alert.accept()
    result = driver.find_element(By.ID,"result")
    assert result.text == "You entered: Abhijeet"
    time.sleep(5)