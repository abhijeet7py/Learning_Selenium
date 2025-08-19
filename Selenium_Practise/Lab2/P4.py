from selenium import webdriver

def prac_4():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")
    page_source = driver.page_source
    print(page_source)
    # assert "Form Authentication" in page_source
    # driver.quit()

prac_4()
