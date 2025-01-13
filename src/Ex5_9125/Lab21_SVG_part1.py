import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_SVG():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    searchbox_element = driver.find_element(By.NAME,"q")
    searchbox_element.send_keys("macmini")

    svg_element = driver.find_elements(By.XPATH,"//*[name()='svg']")
    svg_element[0].click()

    time.sleep(5)