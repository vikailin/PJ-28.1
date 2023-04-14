from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AccountLocators:
    LOCATOR_ACC_INFO_TITLE = (By.CSS_SELECTOR, '.card-title')


class CheckAccountPage(BasePage):
    def check_info_card(self):
        return self.find_element(AccountLocators.LOCATOR_ACC_INFO_TITLE, time=5).text
