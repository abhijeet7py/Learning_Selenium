from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_input_radio_buttons():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    gender = driver.find_element(By.ID,"sex-0")
    gender.click()
    exp =  driver.find_element(By.ID,"exp-3")
    exp.click()
    prof = driver.find_element(By.XPATH,"//input[@id='profession-1']")
    prof.click()
    tool = driver.find_element(By.CSS_SELECTOR,"#tool-2")
    tool.click()
    time.sleep(5)
