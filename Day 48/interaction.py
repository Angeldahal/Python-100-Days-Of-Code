from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_location = "/home/angel/Documents/Python/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_location)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOr, "#articlecount a")
# article_count.click()

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Angel")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Dahal")
email_address = driver.find_element(By.NAME, "email")
email_address.send_keys("Angeldahal@gmail.com")
button = driver.find_element(By.CSS_SELECTOR, ".btn")
button.click()