from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.automation_wrapper import AutomationWrapper


class TestLoginUI(AutomationWrapper):

    def test_title(self):
        actual_title = self.driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        header = self.driver.find_element(By.XPATH, "//h5[contains(@class,'orangehrm-login-title')]").text
        assert_that("Login").is_equal_to(header)

    def test_placeholder(self):
        username_placeholder = self.driver.find_element(By.XPATH, "//input[@name='username']").get_attribute(
            "placeholder")
        assert_that("Username").is_equal_to(username_placeholder)

        username_password = self.driver.find_element(By.XPATH, "//input[@name='password']").get_attribute("placeholder")
        assert_that("Password").is_equal_to(username_password)
