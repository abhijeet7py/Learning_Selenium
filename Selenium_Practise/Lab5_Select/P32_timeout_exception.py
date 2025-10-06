from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException

def test_timeout():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        WebDriverWait(driver=driver,timeout=10).until(
            EC.element_to_be_clickable((By.ID,"Submit")))
    except TimeoutException as te:
        print(te)
        print("Timeout Exception occured! 10 seconds passed...!")
    finally:
        driver.quit()