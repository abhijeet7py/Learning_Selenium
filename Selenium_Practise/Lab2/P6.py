import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options

def practise_Options_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://the-internet.herokuapp.com/")
    title = driver.title
    print(title)

def practise_options_edge():
    edge_options = Options()
    edge_options.add_argument("--incognito")
    driver = webdriver.Edge(options=edge_options)
    driver.get("https://the-internet.herokuapp.com/")
    title = driver.title
    print(title)

practise_Options_chrome()
practise_options_edge()