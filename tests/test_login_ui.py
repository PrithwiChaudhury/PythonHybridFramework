import pytest
from assertpy import assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginUI:

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


    def test_title(self):
        actual_title=self.driver.title
        assert_that("OrangeHRM").is_equal_to(actual_title)



    def test_header(self):
        header=self.driver.find_element(By.XPATH, "//h5[contains(@class,'orangehrm-login-title')]").text
        assert_that("Login").is_equal_to(header)


    def test_placeholder(self):
        username_placeholder=self.driver.find_element(By.XPATH, "//input[@name='username']").get_attribute("placeholder")
        assert_that("Username").is_equal_to(username_placeholder)

        username_password=self.driver.find_element(By.XPATH, "//input[@name='password']").get_attribute("placeholder")
        assert_that("Password").is_equal_to(username_password)




