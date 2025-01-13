import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def exception_handle():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    try:
        element = driver.find_element(By.ID, "this_id_doesnt_exist")
    except NoSuchElementException as nse:
        print(f"Exception caught: {nse}")  # Print exception message

    time.sleep(5)
    driver.quit()