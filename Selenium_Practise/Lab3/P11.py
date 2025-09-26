from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def testP11_linktext():
    driver = webdriver.Chrome()
    driver.get("https://bugbug.io/blog/testing-frameworks/best-selenium-practice-websites/")
    link1 = driver.find_element(By.LINK_TEXT,"The Internet Heroku App")
    link1.click()
    time.sleep(10)
    assert driver.current_url == "https://the-internet.herokuapp.com/"
    time.sleep(10)
