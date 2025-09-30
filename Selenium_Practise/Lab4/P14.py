from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def testP14():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    # first_name = driver.find_element(By.CSS_SELECTOR,"input[id='input-firstname']")
    first_name = driver.find_element(By.CSS_SELECTOR,"#input-firstname")
    first_name.send_keys("Helloo")

    time.sleep(5)

    # #value --> When Id is  present
    # .value --> When class attribute is present
    # Normally --> without // and @ we can write css selector