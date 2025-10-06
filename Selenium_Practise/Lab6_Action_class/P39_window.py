from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
import time

def test_windows_demo():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://demoqa.com/browser-windows")
    driver.maximize_window()
    parent = driver.current_window_handle
    print(parent)
    new_tab = driver.find_element(By.ID,"tabButton")
    new_tab.click()
    window_handles = driver.window_handles
    print(window_handles)
    for handle in window_handles:
        driver.switch_to.window(handle)
        if "This is a sample page" in driver.page_source:
            print("Test case passed!")

    time.sleep(2)
