from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator_type, locator):
        return self.driver.find_element(locator_type, locator)

    def click(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        element.click()

    def enter_text(self, locator_type, locator, text):
        element = self.find_element(locator_type, locator)
        element.clear()
        element.send_keys(text)

