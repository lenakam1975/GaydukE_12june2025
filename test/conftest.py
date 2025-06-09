import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from class_MainPage import MainPage


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def main_page(browser):
    page = MainPage(browser)
    page.open()
    return page


# @pytest.fixture
# def basket_api():
#     basket_api = BasketApi(
#         base_url=BASE_URL,
#         id_cookie=ID_COOKIE,
#         id_product=ID_PRODUCT)
#     return basket_api