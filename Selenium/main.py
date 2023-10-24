import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://63pokupki.ru/auth#/login"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.CLASS_NAME, "spui-Input__input").send_keys("user1049063")
    input2 = browser.find_element(By.XPATH, "//input[@type='password']").send_keys("pass")
    button = browser.find_element(By.CSS_SELECTOR, "button.frm-singIn__btn").click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    browser.quit()

# не забываем оставить пустую строку в конце файла
