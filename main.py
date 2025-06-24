from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import  sleep
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os
load_dotenv()


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
URL = "https://tinder.com/"
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
wait = WebDriverWait(driver, 10)
driver.get(url=URL)
sleep(2)
log_in = driver.find_element(By.XPATH, value='//*[@id="u964729768"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()
sleep(2)
facebook = driver.find_element(By.XPATH, value='//*[@id="u-763651308"]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button')
facebook.click()
sleep(2)

handles = driver.window_handles
print(handles)
base_window = handles[0]
fb_login_window = handles[1]
print(fb_login_window)
driver.switch_to.window(fb_login_window)
print(driver)
print(driver.title)
sleep(5)
cookies = driver.find_element(By.XPATH, value='//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[1]')
cookies.click()
sleep(2)
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
password.send_keys(PASSWORD)
button = driver.find_element(By.XPATH, value='//*[@id="loginbutton"]')
button.click()
sleep(10)
new_window = driver.current_window_handle
continue_ = driver.find_element(By.XPATH, value= '//span[contains(text(), "Continue as")]')
continue_.click()
sleep(5)
driver.switch_to.window(base_window)
phone_number = driver.find_element(By.ID, value="phone_number")
phone_number.send_keys(PHONE_NUMBER)
next_button = driver.find_element(By.XPATH, value='//*[@id="u-763651308"]/div/div/div[2]/div/div[3]/button')
next_button.click()