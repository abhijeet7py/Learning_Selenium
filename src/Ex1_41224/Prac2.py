import time
from selenium import webdriver

def test_prac2():
    driver = webdriver.Chrome()
    driver.get("https://auth.ultimatix.net/utxLogin/login?TYPE=33554432&REALMOID=06-9ed1ab3e-4343-420c-b058-68beeef4c9ff&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-EdbHMX6T%2bWb8DN7DVmL5sbY%2bn%2b30S7n%2fgIBptYa9dLbudResX4AYm9ObPeNozoDH&TARGET=-SM-https%3a%2f%2fwww%2eultimatix%2enet%2f")

    print(driver.title)
    assert driver.title == "Ultimatix - Digitally Connected!"

    time.sleep(5)

    driver.quit()