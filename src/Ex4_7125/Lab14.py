import  time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_5():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name_input = driver.find_element(By.CSS_SELECTOR,"input[name='firstname']")
    first_name_input.send_keys("Hello")

    time.sleep(5)
    driver.quit()