from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def prac_locators1():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    name = driver.find_element(By.ID,"name")
    name.send_keys("Abhijeet")
