import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_select():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    select_element = driver.find_element(By.ID,"dropdown")
    select = Select(select_element)
    # select.select_by_visible_text("Option 2")
    # select.select_by_index(2)

    time.sleep(5)
