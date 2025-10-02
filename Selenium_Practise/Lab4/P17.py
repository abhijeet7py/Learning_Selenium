# Finding element with Ankor tags <a>
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import allure
@pytest.mark.positive
@allure.title("Finding element with Ankor tags <a>")
@allure.description("Finding element with Ankor tags <a>")
def testP16():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/#/login")
    # start = driver.find_element(By.LINK_TEXT,"Start a free trial") # Full match
    start = driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")

    start.click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    driver.back()
    driver.refresh()
    driver.close()