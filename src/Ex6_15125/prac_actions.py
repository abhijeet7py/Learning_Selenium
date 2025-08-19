import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_actions():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    text = driver.find_element(By.ID,"APjFqb")

    actions = ActionChains(driver)
    (actions.move_to_element(text).click().send_keys_to_element(text,"yo")).perform()
    actions.move_to_element(text).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    time.sleep(5)