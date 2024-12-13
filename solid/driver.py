# drivers/browser_driver.py
from selenium import webdriver
from .base import BaseDriver

class ChromeDriver(BaseDriver):
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome()

    def open(self, url):
        super().open(url)


