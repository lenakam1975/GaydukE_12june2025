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
    def add_basket(self) -> requests.Response:
        """ Метод реализует добавление товара в корзину через API
        """
        path =  f"{self.base_url}/ajax/basketOrder.php"
        headers = {
            "Accept-encoding": "gzip, deflate, br, zstd",
            "Accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-length": "92",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Cookie": COOKIE_BASKET,
            "sec-ch-ua":"'Google Chrome';v='137', 'Chromium';v='137', 'Not/A)Brand';v='24'",
            "user-agen": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        data = {
            "idCookie": self.id_cookie,
            "idProd": self.id_product,
            "type":"add"
        }
        response_add = requests.post(path, data=data, headers=headers)
        return response_add

    def plus_basket(self) -> requests.Response:
        """ Метод реализует изменение количества товара в корзине
        """
        path = f"{self.base_url}/ajax/basketOrder.php"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Cookie": COOKIE_BASKET
        }
        data = {
            "idCookie":self.id_cookie,
            "idProd": self.id_product,
            "type": "plus"
        }
        response_plus = requests.post(path, data=data, headers=headers)
        return response_plus

    def delete_basket(self) -> requests.Response:
        """ Метод реализует изменение количества товара в корзине
        """
        path = f"{self.base_url}/ajax/basketOrder.php"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "accept": "application/json",
            "Cookie": COOKIE_BASKET
        }
        data = {
            "idCookie":self.id_cookie,
            "idProd": self.id_product,
            "type": "delete"
        }
        response_del = requests.post(path, data=data, headers=headers)
        return response_del


    def view_basket(self) -> requests.Response:
        """ Метод реализует просмотр состояния корзины
        """
        path = f"{self.base_url}/ajax/basketList.php"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "accept":"application/json",
            "Cookie":COOKIE_BASKET
        }
        response_view = requests.post(path, headers=headers)
        return response_view


