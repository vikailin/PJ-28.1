from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthLocators:
    LOCATOR_AUTH_TYPE_PHONE = (By.ID, 't-btn-tab-phone')
    LOCATOR_AUTH_TYPE_MAIL = (By.ID, 't-btn-tab-mail')
    LOCATOR_AUTH_TYPE_LOGIN = (By.ID, 't-btn-tab-login')
    LOCATOR_AUTH_TYPE_LS = (By.ID, 't-btn-tab-ls')
    LOCATOR_FORGOT_PASSW = (By.ID, 'forgot_password')
    LOCATOR_AGREEMENT = (By.LINK_TEXT, 'пользовательского соглашения' or 'пользовательское соглашение')
    LOCATOR_REGISTRATION = (By.ID, 'kc-register')
    LOCATOR_LOGIN_BUTTON = (By.ID, 'kc-login')
    LOCATOR_VK_BUTTON = (By.ID, 'oidc_vk')
    LOCATOR_ODNOCLASSNIKI_BUTTON = (By.ID, 'oidc_ok')
    LOCATOR_MAILRU_BUTTON = (By.ID, 'oidc_mail')
    LOCATOR_GOOGLE_BUTTON = (By.ID, 'oidc_google')
    LOCATOR_YANDEX_BUTTON = (By.ID, 'oidc_ya')
    LOCATOR_USERNAME_INPUT = (By.ID, 'username')
    LOCATOR_PASSWORD_INPUT = (By.ID, 'password')
    LOCATOR_USERNAME_AND_PASSWORD_WHOLE_FIELDS = (By.CSS_SELECTOR, '.rt-input-container')
    LOCATOR_ERROR_MESSAGE = (By.ID, 'form-error-message')
    LOCATOR_AUTH_FORM = (By.CSS_SELECTOR, '.rt-input-container.tabs-input-container__login')


class CheckAuthPage(BasePage):
    def click_auth_type_phone(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_TYPE_PHONE).click()

    def click_auth_type_mail(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_TYPE_MAIL).click()

    def click_auth_type_login(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_TYPE_LOGIN).click()

    def click_auth_type_ls(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_TYPE_LS).click()

    def click_forgot_password(self):
        return self.find_element(AuthLocators.LOCATOR_FORGOT_PASSW).click()

    def click_agreement(self):
        return self.find_element(AuthLocators.LOCATOR_AGREEMENT).click()

    def click_registration(self):
        return self.find_element(AuthLocators.LOCATOR_REGISTRATION).click()

    def click_login_button(self):
        return self.find_element(AuthLocators.LOCATOR_LOGIN_BUTTON).click()

    def click_vk_button(self):
        return self.find_element(AuthLocators.LOCATOR_VK_BUTTON).click()

    def click_odnoclassniki_button(self):
        return self.find_element(AuthLocators.LOCATOR_ODNOCLASSNIKI_BUTTON).click()

    def click_mailru_button(self):
        return self.find_element(AuthLocators.LOCATOR_MAILRU_BUTTON).click()

    def click_google_button(self):
        return self.find_element(AuthLocators.LOCATOR_GOOGLE_BUTTON).click()

    def click_yandex_button(self):
        return self.find_element(AuthLocators.LOCATOR_YANDEX_BUTTON).click()

    def enter_phone_and_password(self, phone, password):
        self.find_element(AuthLocators.LOCATOR_AUTH_TYPE_PHONE).click()
        user_phone_field = self.find_element(AuthLocators.LOCATOR_USERNAME_INPUT)
        user_phone_field.click()
        user_phone_field.send_keys(phone)
        user_password_field = self.find_element(AuthLocators.LOCATOR_PASSWORD_INPUT)
        user_password_field.click()
        user_password_field.send_keys(password)
        return user_phone_field, user_password_field

    def enter_mail_and_password(self, mail, password):
        self.find_element(AuthLocators.LOCATOR_AUTH_TYPE_MAIL).click()
        user_mail_field = self.find_element(AuthLocators.LOCATOR_USERNAME_INPUT)
        user_mail_field.click()
        user_mail_field.send_keys(mail)
        user_password_field = self.find_element(AuthLocators.LOCATOR_PASSWORD_INPUT)
        user_password_field.click()
        user_password_field.send_keys(password)
        return user_mail_field, user_password_field

    def enter_login_and_password(self, login, password):
        self.find_element(AuthLocators.LOCATOR_AUTH_TYPE_LOGIN).click()
        user_login_field = self.find_element(AuthLocators.LOCATOR_USERNAME_INPUT)
        user_login_field.click()
        user_login_field.send_keys(login)
        user_password_field = self.find_element(AuthLocators.LOCATOR_PASSWORD_INPUT)
        user_password_field.click()
        user_password_field.send_keys(password)
        return user_login_field, user_password_field

    def check_error_message(self):
        return self.find_element(AuthLocators.LOCATOR_ERROR_MESSAGE).text

    def check_username_and_password_fields(self):
        elements_list = self.find_elements(AuthLocators.LOCATOR_USERNAME_AND_PASSWORD_WHOLE_FIELDS)
        return [x.text for x in elements_list]
