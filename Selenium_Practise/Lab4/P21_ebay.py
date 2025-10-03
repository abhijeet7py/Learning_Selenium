# Selenium Project (Mini #2)
#
# 1. Open the Url - [﻿www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067](https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067)
# 2. Search for the Macmini
# 3. Click on the search ICON
# 4. Get all the titles
# 5. Get al the prices
# 6. Print all the titles and prices in the end.

from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import allure
import pytest

def test_Ebay_search():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_box = driver.find_element(By.CSS_SELECTOR,"input[placeholder ='Search for anything']")
    search_box.send_keys("macmini")
    search_button = driver.find_element(By.CSS_SELECTOR,"#gh-search-btn")
    search_button.click()
    time.sleep(5)

    titles = driver.find_elements(By.CSS_SELECTOR,".s-item__title")
    prices = driver.find_elements(By.CSS_SELECTOR,".s-item__price")
    j = 0
    for i in titles:
        print(i.text, "-->" ,prices[j].text)
        j = j + 1


    time.sleep(5)
    driver.quit()
