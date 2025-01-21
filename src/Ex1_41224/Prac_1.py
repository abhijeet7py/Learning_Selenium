from selenium import webdriver

def test_practice1():
    driver = webdriver.Chrome()

    driver.get("https://www.w3resource.com/python-exercises/python-basic-exercises.php")

    # driver_path =

    print(driver.title)
    assert driver.current_url == "https://www.w3resource.com/python-exercises/python-basic-exercises.php"

    driver.quit()