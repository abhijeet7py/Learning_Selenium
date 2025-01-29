import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def prac12():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    buttons = driver.find_elements(By.TAG_NAME,"button")

    print(len(buttons))
    for i in buttons:
        print(i.text)