from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def test_svg_part2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    list_of_states = driver.find_elements(By.XPATH,"//*[local-name()='svg']/*[name()='g'][7]/*[local-name()='g']/*[name()='g']/*[local-name()='path']")
    for states in list_of_states:
        print(states.get_attribute("aria-label"))
        if "Delhi" in states.get_attribute("aria-label"):
            # driver.execute_script("arguments[0].scrollIntoView();", states)
            # driver.execute_script("arguments[0].click();", states)
            states.click()
            break

    time.sleep(5)