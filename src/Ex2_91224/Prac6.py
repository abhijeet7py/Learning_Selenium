import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_chrome_current_url():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    assert driver.current_url == "https://www.saucedemo.com/"

    time.sleep(3)
def test_edge_current_url():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    assert driver.current_url == "https://www.saucedemo.com/"
    time.sleep(3)
def test_safari_current_url():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    assert driver.current_url == "https://www.saucedemo.com/"
    time.sleep(3)

