# Select box & Dropdown (static and dynamic)
#
# 1. HTML Select Tag -
# 2. Dynamic (Custom Dropdown)
#     1. UI -> LI  - List HTML - Handled by using **XPath, JS Executor**

# **Dynamic Cusom Drodowns **- Locate them - Actions (Interactions by using mouse) , JS Executor


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def test_select_static():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    select_box = Select(driver.find_element(By.ID,"dropdown"))
    select_box.select_by_visible_text("Option 2")
    # select_box.select_by_index(2)
    time.sleep(3)
