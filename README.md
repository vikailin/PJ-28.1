PJ-28.1
------------

Репозиторий содержит проект для тестирования интерфейса авторизации в личном кабинете Ростелеком Информационные Технологии.

Ссылка на тестируемый объект:
https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=fdd006af-5db1-46f6-bc54-430dd0e17d59&theme&auth_type

Тесты предназначены для запуска в браузере Google Chrome версии 112.X.XXXX.XX

Файлы
-----

[conftest.py](conftest.py) содержит фикстуру инициализирующую работу драйвера chromedriver для запуска Google Chrome.

[pages/base_page.py](pages/base_page.py) содержит общие методы взаимодействия с элементами страницы.

[pages/auth_page.py](pages/auth_page.py) содержит локаторы элементов и методы взаимодействия с элементами страницы авторизации.

[pages/account_page.py](pages/account_page.py) содержит локаторы элементов и методы взаимодействия с элементами страницы личного кабинет пользователя.

[pages/registration_page.py](pages/registration_page.py) содержит локаторы элементов и методы взаимодействия с элементами страницы регистрации нового пользователя.

[pages/reset_passw_page.py](pages/reset_passw_page.py) содержит локаторы элементов и методы взаимодействия с элементами страницы восстановления пароля пользователя.

[pages/agreement_page.py](pages/agreement_page.py) содержит локаторы элементов и методы взаимодействия с элементами страницы пользовательского соглашения.

[test/tests.py](test/tests.py) содержит набор тестов для объекта, включает 2 группы: тесты авторизации и UI тесты.

[error_screenshots](error_screenshots) папка для сохранения скриншотов при ошибках в тестах авторизации.


Как запустить тесты
-------------------

1) Установить все необходимые зависимости:

    ```bash
    pip3 install -r requirements
    ```

2) Файл Selenium WebDriver - chromedriver приложен к данному проекту

3) Запуск тестов авторизации:
(тесты содержат комментарии, которые сообщают, что условия теста не выполнены и сохранен скриншот страницы)

    ```bash
    python3 pytest -v --driver Chrome --driver-path /chromedriver.exe -m 'auth' test/tests.py -s
    ```
    
4) Запуск тестов UI:

    ```bash
    python3 pytest -v --driver Chrome --driver-path /chromedriver.exe -m 'ui' test/tests.py -s
    ```
    
5) Запуск всех тестов:

    ```bash
    python3 pytest -v --driver Chrome --driver-path /chromedriver.exe test/tests.py -s
    ```
