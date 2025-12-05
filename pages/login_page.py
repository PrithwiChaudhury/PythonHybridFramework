from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class LoginPage(WebDriverKeywords):
    USERNAME_LOCATOR = (By.NAME, "username")
    PASSWORD_LOCATOR = (By.NAME, "password")
    LOGIN_TITLE_LOCATOR = (By.XPATH, "//button[contains(normalize-space(),'Login')]")
    INVALID_ERROR_TEXT = (By.XPATH, "//p[contains(@class,'alert-content-text')]")
    HEADER_TITLE = (By.XPATH, "//h5[contains(@class,'orangehrm-login-title')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver: WebDriver = driver

    def enter_username(self, username):
        # self.__driver.find_element(By.NAME, "username").send_keys(username)
        self.type_on_element(LoginPage.USERNAME_LOCATOR, username)

    def enter_password(self, password):
        # self.__driver.find_element(By.NAME, "password").send_keys(password)
        self.type_on_element(LoginPage.PASSWORD_LOCATOR, password)

    def click_login(self):
        # self.__driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()
        self.click_on_element(LoginPage.LOGIN_TITLE_LOCATOR)

    def get_invalid_error_message(self):
        actual_value = self.get_text_from_element(LoginPage.INVALID_ERROR_TEXT)
        return actual_value

    def get_login_header(self):
        # header = self.driver.find_element(By.XPATH, "//h5[contains(@class,'orangehrm-login-title')]").text
        header = self.get_text_from_element(LoginPage.HEADER_TITLE)
        return header

    def get_username_placeholder(self):
        # username_placeholder = self.__driver.find_element(By.XPATH, "//input[@name='username']").get_attribute(
        #    "placeholder")
        username_placeholder = self.get_attribute_from_element(LoginPage.USERNAME_LOCATOR, "placeholder")
        return username_placeholder

    def get_password_placeholder(self):
        # username_password = self.driver.find_element(By.XPATH, "//input[@name='password']").get_attribute("placeholder")
        username_password = self.get_attribute_from_element(LoginPage.PASSWORD_LOCATOR, "placeholder")
        return username_password
