from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException

def test_stale_exceptions():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        text_area = driver.find_element(By.CSS_SELECTOR,"#APjFqb")
        driver.refresh()
        text_area.send_keys("Abhijeet Jathar")
    except StaleElementReferenceException as sne:
        print(sne)
        print("Stale Element Reference Exception")