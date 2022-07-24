from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
EMAIL = "Angeldahal02@gmail.com"
PASSWORD = "#Angeldahal02"

chrome_driver_path =  "/home/angel/Documents/Python/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.speedtest.net/")


driver.find_element(By.CSS_SELECTOR, ".js-start-test").click()
time.sleep(40)
download_speed = driver.find_element(By.CSS_SELECTOR, ".download-speed").text
upload_speed = driver.find_element(By.CSS_SELECTOR, ".upload-speed").text
driver.get("https://www.twitter.com")
driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a').click()
email = driver.find_element(By.NAME,"text")
email.send_keys(EMAIL)
email.send_keys(Keys.ENTER)
try:
    user_name = driver.find_element(By.NAME, "text")
    user_name.send_keys("angel_dahal1")
    user_name.send_keys(Keys.ENTER)
except :
    pass
password = driver.find_element(By.NAME, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
message= f"My Network Speed is \nDownload Speed: {download_speed}Mbps\nUpload Speed: {upload_speed}Mbps"
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div').click()
tweet = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
tweet.send_keys(message)
driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
