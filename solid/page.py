# pages/login_page.py
from selenium.webdriver.common.by import By
from .base import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")

    def enter_username(self, username):
        self.enter_text(*self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.enter_text(*self.PASSWORD_FIELD, password)

    def submit(self):
        self.click(*self.SUBMIT_BUTTON)


