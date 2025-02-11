from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_webtable_dynamic():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable1.html")

    table = driver.find_element(By.XPATH,"//table[@summary = 'Sample Table']/tbody")
    row_elements = table.find_elements(By.TAG_NAME,"tr")
    # print(len(row_elements))
    # col_elements = driver.find_elements(By.XPATH,"//table[@summery = 'Sample Table']/tbody/tr[1]/td")

    for row in row_elements:
        cols = row.find_elements(By.TAG_NAME,"td")
        for e in cols:
            print(e.text)
