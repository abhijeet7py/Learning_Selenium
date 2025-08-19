import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def test_svg_2():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()

    # driver.switch_to.frame(driver.find_element(By.TAG_NAME,"iframe"))
    # driver.switch_to.frame(0)
    #
    # driver.find_element(By.XPATH,"//button[text()='I understand and agree']").click()
    list_of_states = driver.find_elements(By.XPATH,"//*[name()='svg']"
                                                   "/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    for state in list_of_states:
        print(state.get_attribute("aria-label"))
        if "Maharashtra" in state.get_attribute("aria-label"):
            state.click()
            break
    time.sleep(5)