from selenium import webdriver

def prac2():
    driver = webdriver.Chrome()

    driver.get("file:///C:/Users/Life/Downloads/The%20Ultimate%20Python%20Handbook.pdf")

    title = driver.title
    print(title)
    # assert title == "The Ultimate Python Handbook.pdf"

prac2()