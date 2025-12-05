import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.automation_wrapper import AutomationWrapper
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.data_source import DataSource


class TestLogin(AutomationWrapper):

    @pytest.mark.regression
    @pytest.mark.parametrize("username,password", DataSource.data_valid_login)
    def test_valid_login(self, username, password):
        login = LoginPage(self.driver)
        dashboard = DashboardPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        assert_that(dashboard.get_dashboard_title().is_displayed())

    @pytest.mark.regression
    @pytest.mark.parametrize("username,password,expected_error", [("John", "John123", "Invalid credentials"),
                                                                  ("Saul", "Saul123", "Invalid credentials")])
    def test_invalid_login(self, username, password, expected_error):
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        value = login.get_invalid_error_message()
        assert_that(value).contains(expected_error)

    @pytest.mark.smoke
    def test_title(self):
        actual_title = self.driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    @pytest.mark.smoke
    def test_header(self):
        # header = self.driver.find_element(By.XPATH, "//h5[contains(@class,'orangehrm-login-title')]").text
        login_page = LoginPage(self.driver)
        header = login_page.get_login_header()
        assert_that("Login").is_equal_to(header)

    @pytest.mark.sanity
    def test_placeholder(self):
        login = LoginPage(self.driver)
        username = login.get_username_placeholder()
        assert_that("Username").is_equal_to(username)

        username_password = login.get_password_placeholder()
        assert_that("Password").is_equal_to(username_password)
