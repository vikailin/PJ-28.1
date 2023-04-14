from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ResetPasswLocators:
    LOCATOR_RESET_TITLE = (By.CSS_SELECTOR, '.card-container__title')


class CheckResetPasswPage(BasePage):
    def check_reset_page_title(self):
        return self.find_element(ResetPasswLocators.LOCATOR_RESET_TITLE, time=5).text
