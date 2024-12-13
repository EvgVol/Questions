from abc import ABC, abstractmethod
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class PageInterface(ABC):
    @abstractmethod
    def open(self):
        """Открыть страницу"""
        ...

    @abstractmethod
    def click_element(self, element_id: str):
        """Кликнуть на элемент по ID"""
        ...

    @abstractmethod
    def fill_input(self, element_id: str, value: str):
        """Заполнить поле ввода"""
        ...


class LoginPage(PageInterface):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://example.com/login"

    def open(self):
        self.driver.get(self.url)

    def click_element(self, element_id: str):
        element = self.driver.find_element(By.ID, element_id)
        element.click()

    def fill_input(self, element_id: str, value: str):
        input_field = self.driver.find_element(By.ID, element_id)
        input_field.send_keys(value)



import pytest
from selenium import webdriver

class TestLogin:
    @pytest.fixture(scope="class")
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        yield
        self.driver.quit()

    def test_login(self, setup_class):
        self.login_page.open()
        self.login_page.fill_input("username_id", "test_user")
        self.login_page.fill_input("password_id", "test_password")
        self.login_page.click_element("login_id")
        assert "dashboard" in self.driver.current_url


class RegistrationPage(PageInterface):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://example.com/register"

    def open(self):
        self.driver.get(self.url)

    def click_element(self, element_id: str):
        element = self.driver.find_element(By.ID, element_id)
        element.click()

    def fill_input(self, element_id: str, value: str):
        input_field = self.driver.find_element(By.ID, element_id)
        input_field.send_keys(value)


class TestRegistration:
    @pytest.fixture(scope="class")
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.registration_page = RegistrationPage(self.driver)
        yield
        self.driver.quit()

    def test_registration(self, setup_class):
        self.registration_page.open()
        self.registration_page.fill_input("username", "new_user")
        self.registration_page.fill_input("password", "new_password")
        self.registration_page.click_element("register")
        assert "welcome" in self.driver.current_url