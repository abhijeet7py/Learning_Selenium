import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_prac14():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name = driver.find_element(By.CSS_SELECTOR,"input[name='firstname']")
    first_name.send_keys("Abhijeet")

    time.sleep(2)
    driver.quit()