import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_Actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    first_element = driver.find_element(By.XPATH,"//input[@name='firstname']")

    #Key down --> Pressing a key
    actions = ActionChains(driver=driver)
    (actions.key_down(Keys.SHIFT)
     .send_keys_to_element(first_element,"the testing acadamy")
     .key_up(Keys.SHIFT).perform())

    time.sleep(7)
