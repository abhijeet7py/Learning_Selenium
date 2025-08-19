import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_dynamic_webtables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")
    driver.maximize_window()

    table = driver.find_element(By.XPATH,"//table[@summary = 'Sample Table']/tbody")
    rows = table.find_elements(By.TAG_NAME,"tr")
    for row in rows:
        cols = row.find_elements(By.TAG_NAME,"td")
        for e in cols:
            print(e.text)