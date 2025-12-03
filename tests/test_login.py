from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.automation_wrapper import AutomationWrapper


class TestLogin(AutomationWrapper):

    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        dashboard = self.driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
        assert_that(dashboard.is_displayed())

    def test_invalid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        actual_value = self.driver.find_element(By.XPATH, "//p[contains(@class,'alert-content-text')]").text
        assert_that(actual_value).contains("Invalid")