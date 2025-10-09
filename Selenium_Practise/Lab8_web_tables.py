from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
import time
import pytest

@pytest.mark.parametrize("usr",["Maria Anders", "Roland Mendel", "Yoshi Tannamuri"])
def test_static_webtables(usr):
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()

    row_elements = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    row = len(row_elements)
    # print(row)

    col_elements = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")
    col = len(col_elements)
    # print(col)

    fp = "//table[@id='customers']/tbody/tr["
    sp = "]/td["
    tp = "]"


    for i in range(2, row + 1):
        for j in range(1, col + 1):
            dynamic_path = f"{fp}{i}{sp}{j}{tp}"
            data = driver.find_element(By.XPATH,dynamic_path).text
            # print(data)
            # usr = input("Enter the name: ")
            if usr in data:
                company_path = f"{dynamic_path}/preceding-sibling::td"
                company = driver.find_element(By.XPATH,company_path).text
                country_path = f"{dynamic_path}/following-sibling::td"
                country = driver.find_element(By.XPATH,country_path).text
                print(f"{usr} works at {company} and is in {country}")

    time.sleep(5)
    driver.quit()