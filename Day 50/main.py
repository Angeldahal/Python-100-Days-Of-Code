from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "Angeldahal202@gmail.com"
PASSWORD = "#Angeldahal02"
chrome_driver_path =  "/home/angel/Documents/Python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.tinder.com")

login_button = driver.find_element(By.CSS_SELECTOR, ".button")
login_button.click()
time.sleep(4)
login_with_facebook = driver.find_element(By.XPATH, '//*[@id="q1569938320"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
login_with_facebook.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)
email = driver.find_element(By.NAME, "email")
email.send_keys(EMAIL)
password = driver.find_element(By.NAME, "pass")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
