import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.automation_wrapper import AutomationWrapper
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.data_source import DataSource


class TestLogin(AutomationWrapper):

    @pytest.mark.parametrize("username,password", DataSource.data_valid_login)
    def test_valid_login(self, username, password):

        login = LoginPage(self.driver)
        dashboard = DashboardPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()

        assert_that(dashboard.get_dashboard_title().is_displayed())

    @pytest.mark.parametrize("username,password,expected_error", [("John", "John123", "Invalid credentials"),
                                                                  ("Saul", "Saul123", "Invalid credentials")])
    def test_invalid_login(self, username, password, expected_error):
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()
        value = login.get_invalid_error_message()
        assert_that(value).contains(expected_error)

