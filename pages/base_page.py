from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_' \
                        'b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=' \
                        'openid&state=d3dd47c4-a864-4680-9510-d29ae23d9f38&theme&auth_type'

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not found {locator}')

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Not found {locator}')

    def take_picture(self, name):
        return self.driver.save_screenshot(name)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_second_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])
