import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome(executable_path='/chromedriver')
    yield driver
    driver.quit()
