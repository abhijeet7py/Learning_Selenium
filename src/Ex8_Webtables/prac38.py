import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_webtables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()

    row_elements = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    row = len(row_elements)
    print(row)

    col_elements = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)

    first = "//table[@id='customers']/tbody/tr["
    second = "]/td["
    third = "]"

    for i in range(2, row + 1):
        for j in range(1,col+1):
            dynamic_path = f"{first}{i}{second}{j}{third}"
            data = driver.find_element(By.XPATH,dynamic_path).text
            # print(data, end=" ")
            if "Giovanni Rovelli" in data:
                company_path = f"{dynamic_path}/preceding-sibling::td"
                company = driver.find_element(By.XPATH,company_path).text
                country_path = f"{dynamic_path}/following-sibling::td"
                country = driver.find_element(By.XPATH,country_path).text
                print(f"Giovanni Rovelli works in {company} and is from {country}")
