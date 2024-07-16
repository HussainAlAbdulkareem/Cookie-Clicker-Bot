import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

#Wait for website to load
time.sleep(8)

#Selects English
driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]').click()

time.sleep(5)

cookie_button = driver.find_element(By.ID, value="bigCookie")
cookie_button.click()

num_of_cookies = int(driver.find_element(By.ID, value="cookies").text.split(" ")[0])
print(num_of_cookies)
