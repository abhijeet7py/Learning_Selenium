import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_Keyboard_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    first_element = driver.find_element(By.XPATH,"//input[@name='firstname']")

    actions = ActionChains(driver=driver)
    (actions.key_down(Keys.SHIFT)
     .send_keys_to_element(first_element,"abhijeet").key_up(Keys.SHIFT).send_keys(" jathar").perform())


    time.sleep(5)
    driver.quit()
