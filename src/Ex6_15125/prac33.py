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


def test_heatMap():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/test/ab/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1")
    driver.maximize_window()

    main = driver.current_window_handle

    list = driver.find_elements(By.CSS_SELECTOR,"[data-qa='yedexafobi']")

    variation = list[1]
    variation.click()

    actions = ActionChains(driver)
    actions.click(variation).perform()

    time.sleep(20)

    all_handles = driver.window_handles
    print(all_handles)

    for handle in all_handles:
        if handle != main:
            driver.switch_to.window(handle)
            print(driver.title)
            driver.switch_to.frame("heatmap-iframe")
            click_map = driver.find_element(By.CSS_SELECTOR,"[data-qa = 'liqokuxuba']")
            click_map.click()

            time.sleep(20)


time.sleep(5)



