from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://football360.ir"
driver=webdriver.Chrome()
driver.get(url)


box2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[2]/div[2]/button[1]")))
box2.click()
time.sleep(10)

box1 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/div[1]/div/div/header/div[1]/div/div[1]/div/div/div/input")))
box1.send_keys("پرسپولیس")
box1.send_keys(Keys.ENTER)

input()