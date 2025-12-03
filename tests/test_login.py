import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.automation_wrapper import AutomationWrapper
from utilities.data_source import DataSource


class TestLogin(AutomationWrapper):

    @pytest.mark.parametrize("username,password", DataSource.data_valid_login)
    def test_valid_login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        dashboard = self.driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
        assert_that(dashboard.is_displayed())

    @pytest.mark.parametrize("username,password,expected_error", [("John", "John123", "Invalid credentials"),
                                                                  ("Saul", "Saul123", "Invalid credentials")])
    def test_invalid_login(self, username, password, expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        actual_value = self.driver.find_element(By.XPATH, "//p[contains(@class,'alert-content-text')]").text
        assert_that(actual_value).contains(expected_error)

    @pytest.mark.parametrize("username,password,expected_error", DataSource.data_invalid_login)
    def test_invalid_login_using_data_source(self, username, password, expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        actual_value = self.driver.find_element(By.XPATH, "//p[contains(@class,'alert-content-text')]").text
        assert_that(actual_value).contains(expected_error)


    @pytest.mark.parametrize("username,password,expected_error", DataSource.data_invalid_login_excel)
    def test_invalid_login_using_excel(self, username, password, expected_error):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        actual_value = self.driver.find_element(By.XPATH, "//p[contains(@class,'alert-content-text')]").text
        assert_that(actual_value).contains(expected_error)
