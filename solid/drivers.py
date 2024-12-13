# drivers/base.py
from selenium import webdriver

class BaseDriver:
    def __init__(self):
        self.driver = None

    def open(self, url):
        if self.driver is None:
            raise Exception("Драйвер не инициализирован")
        self.driver.get(url)

    def quit(self):
        if self.driver:
            self.driver.quit()
