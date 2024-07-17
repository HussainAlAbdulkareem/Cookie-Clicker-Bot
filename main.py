import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for website to load
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-EN"]'))).click()

# Wait for the game elements to load
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "bigCookie")))

cookie_button = driver.find_element(By.ID, "bigCookie")
num_of_cookies = 0

i = 0
while True:
    for x in range(100):
        cookie_button.click()
    cookies_text = driver.find_element(By.ID, "cookies").text.split(" ")[0]
    num_of_cookies = float(cookies_text.replace(",", ""))
    option = driver.find_element(By.ID, value=f"product{i}")
    price_text = option.text.split("\n")[1].replace(",", "")
    price = float(price_text)
    if price < num_of_cookies:
        driver.execute_script("arguments[0].click();", option)
        i += 1
    else:
        option = driver.find_element(By.ID, value=f"product{i-1}")
        driver.execute_script("arguments[0].click();", option)
