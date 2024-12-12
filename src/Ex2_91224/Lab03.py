from selenium import webdriver

def test_open_vwo_login():
    driver = webdriver.Chrome() # Crate the session
    driver.get("https://app.vwo.com") # Naviagate to the URL
    page_source_data = driver.page_source # get the page source
    print(page_source_data)