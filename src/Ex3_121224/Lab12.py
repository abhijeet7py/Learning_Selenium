from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_4():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    # buttons = driver.find_elements(By.TAG_NAME,"button")
    # print(len(buttons))
    # for i in buttons:
    #     print(i.text)

    all_links = driver.find_elements(By.TAG_NAME,"a")
    print(len(all_links))
    for i in all_links:
        print(i.text)

# for i in range(10):
#     print(i )