import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException,TimeoutException,NoSuchElementException


def test_Tout_excp_demo():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")

    try:
        WebDriverWait(driver=driver,timeout=10).until(EC.element_to_be_clickable((By.ID,"Submit")))
        print("End of Program")
    except TimeoutException as see:
        print(see)
        print("TimeoutException occured!! , 10 Seconds Passed")
    finally:
        driver.quit()

