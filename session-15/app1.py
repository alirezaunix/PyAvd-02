from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
url="https://www.google.com"

driver.get(url)
driver.maximize_window()
time.sleep(10)

box1 = driver.find_element(
    By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")

box1.send_keys("python")
box1.send_keys(Keys.ENTER)

input()
