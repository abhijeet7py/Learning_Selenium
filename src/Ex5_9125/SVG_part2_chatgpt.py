from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_verify_svg():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")

    # Wait for the SVG element to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[name()='svg']"))
    )

    # Dismiss any potential overlay or wait for it to disappear
    try:
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element((By.ID, "notices"))
        )
    except Exception as e:
        print("Overlay not found or took too long to disappear:", e)

    # Locate the states in the map
    list_of_states = driver.find_elements(By.XPATH,
                                          "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']"
                                          )

    for state in list_of_states:
        aria_label = state.get_attribute("aria-label")
        print(aria_label)
        if "Tripura" in aria_label:
            driver.execute_script("arguments[0].scrollIntoView(true);", state)  # Scroll to the element
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(state))
            state.click()  # Click on the state
            break

    time.sleep(5)
    driver.quit()
