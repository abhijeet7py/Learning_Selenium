import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_prac15():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search = driver.find_element(By.CSS_SELECTOR,"#gh-ac")
    search.send_keys("macmini")

    button = driver.find_element(By.CSS_SELECTOR,"button[value = 'Search']")
    button.click()