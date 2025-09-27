from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import allure
import time

def test_P13():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    f_name = driver.find_element(By.XPATH,"//input[@id= 'input-firstname']")
    f_name.send_keys("Abhijeet")
    time.sleep(10)