import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_mouse_action():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    link = driver.find_element(By.ID,"click")
    link.click()
    WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located((By.ID,"greeting")))
    actions_builder = ActionBuilder(driver=driver)
    (actions_builder.pointer_action.pointer_up(MouseButton.BACK))
    actions_builder.perform()
    time.sleep(3)