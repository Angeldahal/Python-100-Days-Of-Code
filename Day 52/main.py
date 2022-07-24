from selenium import webdriver
from selenium.webdriver.common.by import By
import time
EMAIL = "Angeldahal02@gmail.com"
PASSWORD = "#Angeldahal02"
USERNAME = "leomessi"

chrome_driver_path =  "/home/angel/Documents/Python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.instagram.com")

driver.find_element(By.NAME, 'username').send_keys(EMAIL)
driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "._a9_1").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "._aaw9").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '._aauy').send_keys(USERNAME)
time.sleep(2)
driver.get(f"https://www.instagram.com/{USERNAME}")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,'.oajrlxb2').click()
time.sleep(2)
scrollable_popup = driver.find_element(By.CSS_SELECTOR, '._aano')
for i in range(10):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;", scrollable_popup)
    time.sleep(2)
all_buttons = driver.find_elements(By.CSS_SELECTOR,"li button")
for button in all_buttons:
    try:
        button.click()
        time.sleep(1)
    except :
        cancel_button = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
        cancel_button.click()

