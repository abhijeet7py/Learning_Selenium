from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def test_exception_handle():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    try:
        username = driver.find_element(By.ID, "this doesnt exist")
        username.send_keys("ABC")
    except NoSuchElementException as nse:
        print(f"Exception Caught: {nse}")
