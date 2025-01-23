import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_prac5():
    chrome_options = Options()
    chrome_options.add_argument("--incognito") # Incognoto tab
    # chrome_options.add_argument("--start-maximized") #maximized window size
    # chrome_options.add_argument("--window-size=320,256")
    # chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    time.sleep(5)
    driver.quit()