import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_exceptions():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    element = driver.find_element(By.NAME,"This doesnt exist")
    element.click()
    time.sleep(5)