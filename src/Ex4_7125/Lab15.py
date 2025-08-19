import  time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_6():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    searchbox_element = driver.find_element(By.CSS_SELECTOR,"#gh-ac")
    searchbox_element.send_keys("macmini")

    search_button = driver.find_element(By.CSS_SELECTOR,"button[value = 'Search']")
    search_button.click()

    title_items = driver.find_elements(By.CSS_SELECTOR,".s-item__title")
    price_items =  driver.find_elements(By.CSS_SELECTOR,".s-item__price")
    j = 0
    for i in title_items:
        print(i.text,"-->", price_items[j].text)
        j=j+1

    time.sleep(5)
    driver.quit()