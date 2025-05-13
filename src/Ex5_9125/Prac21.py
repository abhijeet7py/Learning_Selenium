import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_svg():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    search = driver.find_element(By.NAME,"q")
    search.send_keys("macmini")

    svg_1 =  driver.find_elements(By.XPATH,"//*[name()= 'svg']")
    svg_1[0].click()

    time.sleep(5)