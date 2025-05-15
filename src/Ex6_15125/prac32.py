import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys


def test_window_handles():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")

    parent_window = driver.current_window_handle
    print(parent_window)
    link = driver.find_element(By.LINK_TEXT, "Click Here").click()

    windows = driver.window_handles
    print(windows)

    for handle in windows:
        driver.switch_to.window(handle)
        if "New Window" in driver.page_source:
            print("Test Case Passed !")

            break

    time.sleep(5)

