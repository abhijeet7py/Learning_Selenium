from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_trialpage_vwo():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    # LINK_TEXT = EXACT Match
    # free_trial_element = driver.find_element(By.LINK_TEXT,"Start a free trial")
    free_trial_element = driver.find_element(By.PARTIAL_LINK_TEXT,"free trial")
    free_trial_element.click()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(5)
    driver.quit()

# test_trialpage_vwo()

 #<a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">
    # Start a free trial
    # </a>

    # anchor_tag_element = driver.find_element(By.LINK_TEXT,"Start a free trial")
    # anchor_tag_element.click()