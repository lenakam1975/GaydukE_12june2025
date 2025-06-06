import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import *

@allure.epic("Дикий Сбор")
@allure.suite("BasketPage")
class BasketPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = base_url

    def open(self):
        self.driver.get(self.url)

    def click_basket_button(self):
        basket_button = self.driver.find_element(
            By.CSS_SELECTOR, '.bask_btn[onclick="basket_modal(event);"]')
        basket_button.click()

    def click_products(self):
        products_button = self.driver.find_element(
            By.CSS_SELECTOR, 'a[href="#products"]')
        products_button.click()

    def click_up(self):
        self.driver.execute_script("window.scrollBy(0, 1000);")
        wait = WebDriverWait(self.driver, 10)
        button_up = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "up")))
        button_up.click()