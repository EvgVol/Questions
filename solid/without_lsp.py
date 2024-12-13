class TestSearch:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com")

    def teardown_method(self):
        self.driver.quit()

    def test_search(self):
        search_input = self.driver.find_element("search_id")
        search_input.send_keys("query")
        self.driver.find_element("submit_id").click()
        assert self.driver.find_element("results_id").is_displayed()