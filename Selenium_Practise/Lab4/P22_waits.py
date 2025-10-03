# Why we need wait mechanism
import time

# 1. Wait for web element to load
# 2. wait for complete page load
# 3. New frameworks --> reactJs, VueJs, Angular --> uses AJAx (They load the element after sometime)
#     We need to wait for some time to load

# types of wait
# 1. Implicit wait
# 2. Explicit wait
#     a. Fluent wait

### Implicit Wait
# - Selenium Web Driver has borrowed the idea of implicit waits from Watir.
# - Global settings applicable to all elements.
# - **Once it is set** it is applicable to **full automation script.**
# - Different from time.sleep - time.sleep() - It will sleep time for script/ Py Int.


### Explicit Wait
# - Little intelligent wait, wait for certain conditions.
# - **condition you pass it resolves.**
#     - They **allow your code to halt program execution, or freeze the thread, until the**
#
# - Element not visible exception if element not found.
# - Replace Thread.sleep / time.sleep() with explicit wait always.


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_waits():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # driver.implicitly_wait(5)
    # wait = WebDriverWait(driver = driver,timeout= 10)
    username = WebDriverWait(driver=driver,timeout=5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"input[placeholder='Username']")))
    username.send_keys("abc")
    password = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Password']")
    password.send_keys("123")
    login = driver.find_element(By.CSS_SELECTOR,"button[class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
    login.click()
    error = WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located((By.XPATH,"//p[@class = 'oxd-text oxd-text--p oxd-alert-content-text']")))
    print(error.text)
    assert error.text == "Invalid credentials"