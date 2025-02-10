import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.expected_conditions import E\

def test_webtables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()

    # row
    row_elements = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    row = len(row_elements)
    print(row)

    #Col
    col_elements = driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)

    # fp = //table[@id='customers']/tbody/tr[
    # row - 2 - 7
    # SP = ]/td[
    # col - 1 -3
    # TP = ]

    first_part = "//table[@id='customers']/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row + 1):
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(By.XPATH,dynamic_path).text
            if "Roland Mendel" in data:
                company_path = f"{dynamic_path}/preceding-sibling::td"
                company_text = driver.find_element(By.XPATH,company_path).text
                country_path = f"{dynamic_path}/following-sibling::td"
                country_text = driver.find_element(By.XPATH,country_path).text
                print(f"Roland Mendel is in {country_text} from {company_text}")


    time.sleep(3)
    driver.quit()