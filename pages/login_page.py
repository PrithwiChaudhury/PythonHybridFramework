from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.__driver:WebDriver=driver


    def enter_username(self, username):
        self.__driver.find_element(By.NAME, "username").send_keys(username)

    def enter_password(self, password):
        self.__driver.find_element(By.NAME, "password").send_keys(password)

    def click_login(self):
        self.__driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Login')]").click()

    def get_invalid_error_message(self):
        actual_value = self.__driver.find_element(By.XPATH, "//p[contains(@class,'alert-content-text')]").text
        return actual_value

    def get_login_header(self):
        pass

    def get_username_placeholder(self):
        username_placeholder = self.__driver.find_element(By.XPATH, "//input[@name='username']").get_attribute(
            "placeholder")
        return username_placeholder

    def get_password_placeholder(self):
        username_password = self.driver.find_element(By.XPATH, "//input[@name='password']").get_attribute("placeholder")
        return username_password