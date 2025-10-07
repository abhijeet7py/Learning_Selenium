from openpyxl.styles.builtins import title
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton
import time

def test_JS_P1():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.smashingmagazine.com/2017/05/long-scrolling/")
    driver.maximize_window()
    driver.execute_script("window.scrollBy(0, 1000);")
    title = driver.execute_script("return document.title;")
    print(title)
    url = driver.execute_script("return document.URL")
    print(url)

    time.sleep(3)