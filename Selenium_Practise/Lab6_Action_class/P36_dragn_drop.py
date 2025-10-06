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

def test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    drag = driver.find_element(By.ID,"draggable")
    drop = driver.find_element(By.ID,"droppable")

    actions = ActionChains(driver=driver)
    actions.drag_and_drop(drag,drop).perform()
    result = WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located(
        (By.ID,"drop-status")))
    print(result.text)
    assert result.text == "dropped"
    time.sleep(3)