import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


def test_stale_excp_demo():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")

    try:
        textarea = driver.find_element(By.NAME, "q")
        driver.refresh()
        textarea.send_keys("hii")
    except StaleElementReferenceException as see:
        print(see)
        print("Stale element exception")

    time.sleep(5)
