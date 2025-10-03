from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import allure

 # 1.id --> #id
 # 2. class --> .className

 # css selector --> Only couple of functions are available
 # awesomeqa.com/css
 # element --> div.first span
def testP20_css_selector():
    # chrome_options = Options()
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/css/")
    span1 = driver.find_element(By.CSS_SELECTOR,"div.first span:first-child")
    span7 = driver.find_element(By.CSS_SELECTOR,"div.first span:last-child")

    span3 = driver.find_element(By.CSS_SELECTOR,"div.first span:nth-child(3)")

    spans_odd = driver.find_elements(By.CSS_SELECTOR,"div.first span:nth-child(2n +1)") # Odd numbers
    spans_even = driver.find_elements(By.CSS_SELECTOR,"div.first span:nth-child(2n)") # Even numbers

    # print(span1.text)
    # print(span7.text)
    # print(span3.text)
    for i in spans_even:
        print(i.text)


# image = img[title = "Flipkart"] --> Exact match
# image = img[title* = "Flip"] --> * --> Contains --> partial match
# image = img[title ^= "Flip"] -> ^ --> starts-with --> Xpath
# image =  img[title $= "art"] -> $ --> ends-with 