from selenium.webdriver.common.by import By
from base.webdriver_keywords import WebDriverKeywords


class DashboardPage(WebDriverKeywords):

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver

    def get_quick_launch_text(self):
        pass

    def get_dashboard_title(self):
        dashboard = self.__driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
        return dashboard
