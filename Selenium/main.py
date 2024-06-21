import random

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://63pokupki.ru/auth#/login"


def generator_pwd(num):
    return ''.join(
        [random.choice(
            list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
        ) for x in range(num)]
    )


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "spui-Input__input").send_keys("user1049063")
    for i in range(5):
        browser.find_element(By.XPATH, "//input[@type='password']").send_keys(generator_pwd(6))
        browser.find_element(By.CSS_SELECTOR, "button.frm-singIn__btn").click()


finally:
    time.sleep(30)
    browser.quit()
