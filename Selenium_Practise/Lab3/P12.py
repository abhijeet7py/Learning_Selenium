from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def testP12():
    driver = webdriver.Chrome()
    driver.get("https://bugbug.io/blog/testing-frameworks/best-selenium-practice-websites/")

    all_links = driver.find_elements(By.TAG_NAME,"a")
    print(len(all_links))
    for i in all_links:
        print(i.text)