from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def practise_chrome_options():
    chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1200,900")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://the-internet.herokuapp.com/")
    title = driver.title
    print(title)

    # driver.quit()

practise_chrome_options()