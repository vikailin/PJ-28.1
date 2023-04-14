import pytest

from pages.agreement_page import CheckAgreementPage
from pages.auth_page import CheckAuthPage
from pages.account_page import CheckAccountPage
from pages.registration_page import CheckRegisterPage
from pages.reset_passw_page import CheckResetPasswPage
from settings import *


@pytest.mark.auth
@pytest.mark.parametrize('phone', [valid_phone, invalid_phone, ''], ids=['valid phone', 'invalid phone', 'empty phone'])
@pytest.mark.parametrize('password', [valid_password, invalid_password, ''], ids=['valid password', 'invalid password',
                                                                                  'empty password'])
def test_auth_with_phone(browser, phone, password):
    auth_page = CheckAuthPage(browser)
    account_page = CheckAccountPage(browser)
    auth_page.go_to_site()
    auth_page.enter_phone_and_password(phone, password)
    auth_page.click_login_button()
    if phone == valid_phone and password == valid_password:
        try:
            info_card = account_page.check_info_card()
            assert 'Учетные данные' in info_card
        except Exception:
            account_page.take_picture(f'error_screenshots/error with {phone} and {password}.png')
            print('ошибка авторизации с валидными данными, сделан скриншот')

    else:
        try:
            error = auth_page.check_error_message()
            assert 'Неверный логин или пароль' in error
        except Exception:
            auth_page.take_picture(f'error_screenshots/error with {phone} and {password}.png')
            print('ошибка ошибка авторизации с невалидными данными номер, сделан скриншот')


@pytest.mark.auth
@pytest.mark.parametrize('mail', [valid_mail, invalid_mail, ''], ids=['valid mail', 'invalid mail', 'empty mail'])
@pytest.mark.parametrize('password', [valid_password, invalid_password, ''], ids=['valid password', 'invalid password',
                                                                                  'empty password'])
def test_auth_with_mail(browser, mail, password):
    auth_page = CheckAuthPage(browser)
    account_page = CheckAccountPage(browser)
    auth_page.go_to_site()
    auth_page.click_auth_type_mail()
    auth_page.enter_mail_and_password(mail, password)
    auth_page.click_login_button()
    if mail == valid_mail and password == valid_password:
        try:
            info_card = account_page.check_info_card()
            assert 'Учетные данные' in info_card
        except Exception:
            account_page.take_picture(f'error_screenshots/error with {mail} and {password}.png')
            print('ошибка авторизации с валидными данными, сделан скриншот')
    else:
        try:
            error = auth_page.check_error_message()
            assert 'Неверный логин или пароль' in error
        except Exception:
            auth_page.take_picture(f'error_screenshots/error with {mail} and {password}.png')
            print('ошибка ошибка авторизации с невалидными данными, сделан скриншот')


@pytest.mark.auth
@pytest.mark.parametrize('login', [valid_login, invalid_login, ''], ids=['valid login', 'invalid login', 'empty login'])
@pytest.mark.parametrize('password', [valid_password, invalid_password, ''], ids=['valid password', 'invalid password',
                                                                                  'empty password'])
def test_auth_with_login(browser, login, password):
    auth_page = CheckAuthPage(browser)
    account_page = CheckAccountPage(browser)
    auth_page.go_to_site()
    auth_page.click_auth_type_login()
    auth_page.enter_login_and_password(login, password)
    auth_page.click_login_button()
    if login == valid_login and password == valid_password:
        try:
            info_card = account_page.check_info_card()
            assert 'Учетные данные' in info_card
        except Exception:
            account_page.take_picture(f'error_screenshots/error with {login} and {password}.png')
            print('ошибка авторизации с валидными данными, сделан скриншот')
    else:
        try:
            error = auth_page.check_error_message()
            assert 'Неверный логин или пароль' in error
        except Exception:
            auth_page.take_picture(f'error_screenshots/error with {login} and {password}.png')
            print('ошибка ошибка авторизации с невалидными данными, сделан скриншот')


@pytest.mark.ui
def test_check_phone_auth_type_elements(browser):
    auth_page = CheckAuthPage(browser)
    auth_page.go_to_site()
    fields = auth_page.check_username_and_password_fields()
    assert 'Мобильный телефон' and 'Пароль' in fields


@pytest.mark.ui
def test_check_mail_auth_type_elements(browser):
    auth_page = CheckAuthPage(browser)
    auth_page.go_to_site()
    auth_page.click_auth_type_mail()
    fields = auth_page.check_username_and_password_fields()
    assert 'Электронная почта' and 'Пароль' in fields


@pytest.mark.ui
def test_check_login_auth_type_elements(browser):
    auth_page = CheckAuthPage(browser)
    auth_page.go_to_site()
    auth_page.click_auth_type_login()
    fields = auth_page.check_username_and_password_fields()
    assert 'Логин' and 'Пароль' in fields


@pytest.mark.ui
def test_check_ls_auth_type_elements(browser):
    auth_page = CheckAuthPage(browser)
    auth_page.go_to_site()
    auth_page.click_auth_type_ls()
    fields = auth_page.check_username_and_password_fields()
    assert 'Личевой счет' and 'Пароль' in fields


@pytest.mark.ui
def test_check_vk_button(browser):
    auth_page = CheckAuthPage(browser)
    auth_page.go_to_site()
    auth_page.click_vk_button()
    vk_page = auth_page.get_current_url()
    assert 'vk.com' in vk_page


@pytest.mark.ui
def test_check_odnoclassniki_button(browser):
    auth_page = CheckAuthPage(browser)
    auth_page.go_to_site()
    auth_page.click_odnoclassniki_button()
    odnoclassniki_page = auth_page.get_current_url()
    assert 'ok.ru' in odnoclassniki_page


@pytest.mark.ui
def test_check_mailru_button(browser):
    auth_page = CheckAuthPage(browser)
    auth_page.go_to_site()
    auth_page.click_mailru_button()
    mailru_page = auth_page.get_current_url()
    assert 'mail.ru' in mailru_page


@pytest.mark.ui
def test_check_google_button(browser):
    auth_page = CheckAuthPage(browser)
    auth_page.go_to_site()
    auth_page.click_google_button()
    google_page = auth_page.get_current_url()
    assert 'google.com' in google_page


@pytest.mark.ui
@pytest.mark.xfail
def test_check_yandex_button(browser):
    auth_page = CheckAuthPage(browser)
    auth_page.go_to_site()
    auth_page.click_yandex_button()
    yandex_page = auth_page.get_current_url()
    assert 'yandex.ru' in yandex_page


@pytest.mark.ui
def test_check_forgot_paswword_button(browser):
    auth_page = CheckAuthPage(browser)
    reset_passw_page = CheckResetPasswPage(browser)
    auth_page.go_to_site()
    auth_page.click_forgot_password()
    reset_page_title = reset_passw_page.check_reset_page_title()
    assert 'Восстановление пароля' in reset_page_title
    assert 'reset' in reset_passw_page.get_current_url()


@pytest.mark.ui
def test_check_registration_button(browser):
    auth_page = CheckAuthPage(browser)
    register_page = CheckRegisterPage(browser)
    auth_page.go_to_site()
    auth_page.click_registration()
    register_page_title = register_page.check_register_page_title()
    assert 'Регистрация' in register_page_title
    assert 'registration' in register_page.get_current_url()


@pytest.mark.ui
def test_check_agreement_button(browser):
    auth_page = CheckAuthPage(browser)
    agreement_page = CheckAgreementPage(browser)
    auth_page.go_to_site()
    auth_page.click_agreement()
    agreement_page.switch_to_second_window()
    agreement_page_title = agreement_page.check_agreement_page_title()
    assert 'Пользовательское соглашение' or 'Пользовательского соглашения' in agreement_page_title
    assert 'agreement' in agreement_page.get_current_url()
