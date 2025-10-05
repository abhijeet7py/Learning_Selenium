from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_svg_part2_prac():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.worldometers.info/coronavirus/")
    list_of_cases = driver.find_elements(By.XPATH,"//div[@id='highcharts-6fsi40z-7713']//*[name()='svg']/*[name()='g'][5]/*[name()='g'][1]/*[name()='rect']")
    actions = ActionChains(driver=driver)
    for cases in list_of_cases:
        # time.sleep(3)
        actions.move_to_element(cases).perform()

    time.sleep(2)
