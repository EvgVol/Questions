class LoginPage:
    def __init__(self, driver: webdriver):
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


class TestLogin:
    @pytest.fixture(scope="class")
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        yield
        self.driver.quit()

    def test_login(self, setup_class):
        self.login_page.open()
        self.login_page.fill_input("username", "test_user")
        self.login_page.fill_input("password", "test_password")
        self.login_page.click_element("login")
        assert "dashboard" in self.driver.current_url

