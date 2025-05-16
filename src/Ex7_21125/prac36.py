import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_shadowDOM():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()
    username_div = driver.find_element(By.XPATH,"//div[@id='userName']")
    driver.execute_script("arguments[0].scrollIntoView(true);",username_div)
    time.sleep(5)
    # document.querySelector('div#userName').shadowRoot.querySelector('#kils');
    username = driver.execute_script("return document.querySelector('div#userName').shadowRoot.querySelector('#kils');")
    username.send_keys("Abhijeet")

    pizza = driver.execute_script(
        "return document.querySelector('div#userName').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza');")
    # document.querySelector('div#userName').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza');
    pizza.send_keys("Chiken")
    time.sleep(5)
