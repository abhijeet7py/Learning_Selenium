import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_selectbox():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    select_box = driver.find_element(By.ID,"dropdown")
    select = Select(select_box)
    # select.select_by_index(0)
    # select.select_by_visible_text("Option 2")
    select.select_by_value("2")
    time.sleep(5)