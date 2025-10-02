import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import allure
@pytest.mark.positive
@allure.title("Finding all the buttons and links in a page")
@allure.description("Finding all the buttons and links in a page")
def testP16():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/#/login")
    # all_buttons = driver.find_elements(By.TAG_NAME,"button")
    # print(len(all_buttons))
    # for i in all_buttons:
    #     print(i.text)
    all_links = driver.find_elements(By.TAG_NAME,"a")
    print(len(all_links))
    for i in all_links:
        print(i.text)