from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationLocators:
    LOCATOR_REGISTER_TITLE = (By.CSS_SELECTOR, '.card-container__title')


class CheckRegisterPage(BasePage):
    def check_register_page_title(self):
        return self.find_element(RegistrationLocators.LOCATOR_REGISTER_TITLE, time=5).text
