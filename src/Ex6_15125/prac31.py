import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException,StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.keys import Keys

def test_make_my_trip():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    WebDriverWait(driver=driver,timeout=5).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']")))

    close =  driver.find_element(By.XPATH,"//span[@data-cy='closeModal']").click()

    from_city = driver.find_element(By.ID,"fromCity")
    actions = ActionChains(driver)
    (actions.move_to_element(from_city).click().send_keys_to_element(from_city,"del").perform())
    time.sleep(2)
    (actions.move_to_element(from_city).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform())

    time.sleep(5)