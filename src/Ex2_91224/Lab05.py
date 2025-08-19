from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

def test_chrome_options():
    chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--window-size=900,800")
    # chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    time.sleep(5)
    driver.quit()
    # assert True == False

# test_chrome_options()