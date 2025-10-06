from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
import time

def test_keyboard_demo():
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    driver.get("https://demo.opencart.com/")

    desktop = WebDriverWait(driver=driver,timeout=30).until(
        EC.element_to_be_clickable((By.LINK_TEXT,"Desktops")))
    desktop.click()

    time.sleep(2)