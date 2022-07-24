from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path =  "/home/angel/Documents/Python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

email = driver.find_element(By.NAME, "session_key")
email.send_keys("angeldahal02@gmail.com")

password = driver.find_element(By.NAME, "session_password")
password.send_keys("!!emA9b?*59J7/e")

driver.find_element(By.CSS_SELECTOR, ".btn__primary--large").click()


