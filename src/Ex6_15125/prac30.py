import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.keys import Keys


def test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    drag = driver.find_element(By.ID,"draggable")
    drop = driver.find_element(By.ID,"droppable")

    actions = ActionChains(driver=driver)
    actions.drag_and_drop(drag,drop).perform()

    time.sleep(5)