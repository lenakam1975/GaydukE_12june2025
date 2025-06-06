import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@allure.epic("Дикий Сбор")
@allure.suite("MainPage")
class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.sibdar-spb.ru/"

    def open(self):
        self.driver.get(self.url)

    def open_basket(self):
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

    def add_to_basket(self):
        self.driver.execute_script("window.scrollBy(0, 1000);")
        button_add = self.driver.find_element(
            By.XPATH, "//button[@onclick=\"addToCard('204', this, event);\"]")
        button_add.click()

    def check_quantity_to_basket(self):
        element = self.driver.find_element(By.ID, "count_product_item_204")
        text_content = element.get_attribute('value')
        return text_content

    def input_text(self, name, phone):
        input_name = self.driver.find_element(By.CSS_SELECTOR, ".req_bask.name_order_bask")
        input_name.clear()
        input_name.send_keys(name)
        input_phone = self.driver.find_element(By.CSS_SELECTOR, ".ph.req_bask.phone_order_bask")
        input_phone.clear()
        input_phone.send_keys(str(phone))
        return name, phone

    def button_send(self):
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn_fill.js-fast-order-btn")
        element.click()


