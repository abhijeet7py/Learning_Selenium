import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_actions_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    first_name = driver.find_element(By.CSS_SELECTOR,"input[name='firstname']")

    actions = ActionChains(driver=driver)
    (actions.key_down(Keys.SHIFT).
     send_keys_to_element(first_name,"abhijeet jathar")
     .key_up(Keys.SHIFT).perform())

    time.sleep(5)