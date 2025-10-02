from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def testP15():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.ebay.com/")
    search_box = driver.find_element(By.CSS_SELECTOR,"#gh-ac")
    search_box.send_keys("iPhone")
    search = driver.find_element(By.CSS_SELECTOR,"#gh-search-btn")
    search.click()
    time.sleep(5)
