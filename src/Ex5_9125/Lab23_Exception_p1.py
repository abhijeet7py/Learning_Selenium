import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_exception():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    element = driver.find_element(By.ID,"This id Doesn't exist")
    # response = {'status': 404, 'value':
    # '{"value":{"error":"no such element",
    # "message":"no such element: Unable to locate element:

    # No such element exception
    time.sleep(5)
