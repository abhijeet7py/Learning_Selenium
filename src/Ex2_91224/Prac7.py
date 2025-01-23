import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_prac7():
    driver = webdriver.Chrome()
    driver.get("https://www.demoblaze.com/index.html")

    join_element = driver.find_element(By.LINK_TEXT,"Cart")
    join_element.click()

    assert driver.current_url == "https://www.demoblaze.com/cart.html"

    time.sleep(3)
    driver.quit()