# tests/conftest.py
import pytest
from drivers.browser_driver import ChromeDriver

@pytest.fixture
def browser():
    driver = ChromeDriver()
    driver.open("https://example.com")
    yield driver
    driver.quit()

