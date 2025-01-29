import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def prac_11():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # link_element = driver.find_element(By.LINK_TEXT,"Start a free trial")
    link_element = driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
    link_element.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(3)
    driver.quit()
