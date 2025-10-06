from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException

def test_exception():
    driver = webdriver.Chrome()
    driver.get("https://www.python.org")
    element = driver.find_element(By.ID, "q")
    element.click()

    # {'status': 404,
    #  'value': '{"value":{"error":"no such element","message":'
    #           '"no such element: Unable to locate element: