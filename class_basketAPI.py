import requests
import allure

from constants import *


@allure.epic("Дикий Сбор")
@allure.suite("BasketApi")
class BasketApi:
    def __init__(self, base_url=BASE_URL, id_cookie=ID_COOKIE, id_product=ID_PRODUCT) -> None:
        self.base_url = base_url
        self.id_cookie = id_cookie
        self.id_product = id_product

    @allure.step(f'[API].Добавить товар с id {ID_PRODUCT} в корзину')
    def add_basket(self, id_prod=ID_PRODUCT) -> tuple[str, int]:
        """ Метод реализует добавление товара в корзину через API
        """
        path = f"{self.base_url}/ajax/basketOrder.php"
        headers = {
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Cookie":COOKIE,
            "connection": "keep-alive",
            "content-length": "87",
            "x-requested-with": "XMLHttpRequest",
            "referer": "https://www.sibdar-spb.ru",
            "origin": "https://www.sibdar-spb.ru"
        }
        data = {
            "idCookie":self.id_cookie,
            "idProd":id_prod,
            "type":"add",
        }
        response = requests.post(path, data=data, headers=headers)
        return response.text, response.status_code


    def plus_basket(self, id_prod=ID_PRODUCT) -> str:
        """ Метод реализует изменение количества товара в корзине
        """
        path = f"{self.base_url}/ajax/basketOrder.php"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Cookie": COOKIE,
            "connection": "keep-alive",
            "content-length": "87",
            "x-requested-with": "XMLHttpRequest",
            "referer": "https://www.sibdar-spb.ru",
            "origin": "https://www.sibdar-spb.ru"
        }
        data = {
            "idCookie":self.id_cookie,
            "idProd": id_prod,
            "type": "plus"
        }
        response_plus = requests.post(path, data=data, headers=headers)
        return response_plus.text

    def delete_basket(self, id_prod=ID_PRODUCT) -> str:
        """ Метод реализует изменение количества товара в корзине
        """
        path = f"{self.base_url}/ajax/basketOrder.php"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "accept": "application/json"
        }
        data = {
            "idCookie":self.id_cookie,
            "idProd": id_prod,
            "type": "plus"
        }
        response_plus = requests.post(path, data=data, headers=headers)
        return response_plus.text

    def view_basket(self) -> str:
        """ Метод реализует просмотр состояния корзины
        """
        path = f"{self.base_url}/ajax/basketList.php"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "accept":"application/json",
            "Cookie":COOKIE_BASKET
        }
        response_view = requests.post(path, headers=headers)
        return response_view.text


