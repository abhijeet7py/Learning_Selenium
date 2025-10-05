from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def test_svg_part1():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    search = driver.find_element(By.XPATH,"//input[@name='q']")
    search.send_keys("macmini")

    # list_of_svg = driver.find_elements(By.XPATH,"//*[local-name()='svg']")
    list_of_svg = driver.find_elements(By.XPATH,"//*[name()='svg']")
    list_of_svg[0].click()
    time.sleep(5)