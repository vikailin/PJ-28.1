from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AgreementLocators:
    LOCATOR_AGREEMENT_TITLE = (By.CSS_SELECTOR, '.offer-title')


class CheckAgreementPage(BasePage):
    def check_agreement_page_title(self):
        return self.find_element(AgreementLocators.LOCATOR_AGREEMENT_TITLE, time=5).text
