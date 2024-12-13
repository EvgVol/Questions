class TestSearch(BaseTest):
    def create_driver(self):
        return webdriver.Chrome()

    def test_search(self):
        search_input = self.driver.find_element("search_id")
        search_input.send_keys("query")
        self.driver.find_element(By.NAME, "submit").click()
        assert self.driver.find_element(By.ID, "results").is_displayed()