from selenium import webdriver

def test_task2():
    driver = webdriver.Chrome() # Create the session
    driver.get("https://katalon-demo-cura.herokuapp.com/") # Navigate to URL
    page_source_data = driver.page_source
    assert "CURA Healthcare Service" in page_source_data
    driver.quit()