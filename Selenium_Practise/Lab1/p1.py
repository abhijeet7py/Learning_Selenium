from selenium import webdriver

def prac1():
    # Creating an object of driver
    driver = webdriver.Chrome()
    # Navigating to the Url
    driver.get("https://github.com/CodeWithHarry/The-Ultimate-Python-Course/blob/main/Chapter%209%20-%20PS/11_problem.py")

    # Get title of page
    print(driver.title)

    assert driver.current_url == "https://github.com/CodeWithHarry/The-Ultimate-Python-Course/blob/main/Chapter%209%20-%20PS/11_problem.py"

prac1()