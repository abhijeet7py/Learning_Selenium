import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException

def test_exception_handle():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    try:
        element = driver.find_element(By.NAME,"No element")

        element.click()
    except NoSuchElementException as nse:
        print(nse.msg)

    time.sleep(5)