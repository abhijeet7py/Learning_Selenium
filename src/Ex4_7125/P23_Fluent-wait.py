from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException)

def test_fluent_wait():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    igored_list = [ElementNotVisibleException,NoSuchElementException,ElementNotSelectableException]

    #Fluent wait
    username = WebDriverWait(driver=driver, poll_frequency=1 , timeout=5,ignored_exceptions=igored_list).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Username']")))
    username.send_keys("Admin")
    password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
    password.send_keys("admin123")
    login = driver.find_element(By.CSS_SELECTOR,
                                "button[class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    login.click()

    dash = WebDriverWait(driver=driver,poll_frequency=1,timeout=5,ignored_exceptions=igored_list).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,".oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module"))
    )
    print(dash.text)
    assert dash.text == "Dashboard"
    # error = WebDriverWait(driver=driver, timeout=5).until(
    #     EC.visibility_of_element_located((By.XPATH, "//p[@class = 'oxd-text oxd-text--p oxd-alert-content-text']")))
    # print(error.text)
    # assert error.text == "Invalid credentials"