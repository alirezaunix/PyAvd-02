from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

delay_time = 10
birthyear = input("Please Your Enter Birth Year: ")
gender = input("Please Your Enter Gender(m/f): ")
gender = "مرد" if gender == "m" else "زن"


options = Options()
service = Service('')
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://esanj.ir/myers-briggs-type-indicator-mbti')

btn_1 = WebDriverWait(driver, delay_time).until(
    EC.element_to_be_clickable(
        (By.XPATH,  '/html/body/main/div[2]/div/div[4]/div/div/div[2]/a[1]'))
)
btn_1.click()

btn_2 = WebDriverWait(driver, delay_time).until(
    EC.element_to_be_clickable(
        (By.XPATH,  '/html/body/main/div[5]/div/div[1]/div[2]/div/div[1]/div'))
)
btn_2.click()

sel_1 = WebDriverWait(driver, delay_time).until(EC.element_to_be_clickable((
    By.XPATH, '/html/body/main/div[5]/div/div[1]/div[4]/form/div[1]/label[1]/select')))
Select(sel_1).select_by_value(birthyear)

sel_2 = WebDriverWait(driver, delay_time).until(EC.element_to_be_clickable((
    By.XPATH, '/html/body/main/div[5]/div/div[1]/div[4]/form/div[1]/label[2]/select')))
Select(sel_2).select_by_visible_text(gender)

btn_3 = WebDriverWait(driver, delay_time).until(
    EC.element_to_be_clickable(
        (By.XPATH,  '/html/body/main/div[5]/div/div[1]/div[4]/form/div[2]/button'))
)
btn_3.click()

radio_text = "دشوار است"
radio_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, f'/html/body/main/section/div[3]/label[contains(text(), "{radio_text}")]'))
)
radio_button.click()
'''


time.sleep(20)
'''

input()