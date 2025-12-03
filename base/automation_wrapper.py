import pytest
from selenium import webdriver


class AutomationWrapper:

    @pytest.fixture(scope="function", autouse=True)
    def set_up(self):
        # runs before each test
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        # runs after each test even if test fails
        self.driver.quit()
