import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_JS_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # Click on the element and check the results (Assertion result)

    alert_element = driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
    alert_element.click()

    (WebDriverWait(driver=driver,timeout=3).until(EC.alert_is_present()))

    alert = driver.switch_to.alert

    alert.accept()

    result_text  = driver.find_element(By.ID,"result").text
    assert result_text == "You successfully clicked an alert"

    time.sleep(5)

def test_alerts_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    confirm_alert = driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
    confirm_alert.click()

    (WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present()))

    alert = driver.switch_to.alert
    # alert.accept()
    alert.dismiss()

    result_text  = driver.find_element(By.ID,"result").text
    # assert result_text == "You clicked: Ok"
    assert result_text == "You clicked: Cancel"


    time.sleep(5)

def test_alerts_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    confirm_alert = driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
    confirm_alert.click()

    (WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present()))

    alert = driver.switch_to.alert
    alert.send_keys("Abhijeet")
    alert.accept()
    # alert.dismiss()

    result_text  = driver.find_element(By.ID,"result").text
    assert result_text == "You entered: Abhijeet"
    # assert result_text == "You entered: null"

    time.sleep(5)
