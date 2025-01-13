import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException

def stale_exception():
    driver =  webdriver.Chrome()
    driver.get("https://google.com")
    try:
        text_area = driver.find_element(By.NAME,"q")
        driver.refresh()
        text_area.send_keys("Abhijeet Jathar")


    except StaleElementReferenceException as see:
        print(see)
        print("Stale element reference")

    time.sleep(3)
