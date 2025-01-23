import time
from selenium import webdriver

def test_prac4():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")
    page_source = driver.page_source
    assert "Elements" in page_source
    print(page_source)

    time.sleep(3)
    driver.quit()