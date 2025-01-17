import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_click_and_hold():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    drag_element = driver.find_element(By.ID,"draggable")

    time.sleep(2)

    actions = ActionChains(driver)
    actions.click_and_hold(on_element=drag_element).perform()

    time.sleep(5)