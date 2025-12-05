import pytest
from selenium import webdriver

from utilities import data_reader


class AutomationWrapper:

    @pytest.fixture(scope="function", autouse=True)
    def set_up(self):
        # runs before each test

        browser_name: str = data_reader.get_value_from_json_config("browser")
        url: str = data_reader.get_value_from_json_config("url")

        if browser_name.lower() == "edge":
            self.driver = webdriver.Edge()
        elif browser_name.lower() == "ff":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        yield
        # runs after each test even if test fails
        self.driver.quit()
