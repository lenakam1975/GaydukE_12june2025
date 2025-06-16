import requests
import allure
import json


from constants import BASE_URL, ID_COOKIE, ID_PRODUCT, COOKIE_BASKET, cookie_view


@allure.epic("Дикий Сбор")
@allure.suite("BasketApi")
class BasketApi:
    def __init__(self,
                 base_url=BASE_URL,
                 id_cookie=ID_COOKIE,
                 id_product=ID_PRODUCT
                 ) -> None:
        self.base_url = base_url
        self.id_cookie = id_cookie
        self.id_product = id_product

    def add_basket(self) -> requests.Response:
        """ Метод реализует добавление товара в корзину
        """
        path = f"{self.base_url}/ajax/basketOrder.php"
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": self.base_url,
            "Referer": f"{self.base_url}/",
            "Cookie": COOKIE_BASKET
        }
        encoded_body = {
            "data": json.dumps({
                "idCookie": self.id_cookie,
                "idProd": str(self.id_product),
                "type": "add"
            })
        }
        response = requests.post(path, headers=headers, data=encoded_body)
        print("status:", response.status_code)
        print("text:", repr(response.text))
        print("headers:", response.headers)
        return response

    def plus_basket(self) -> requests.Response:
        """ Метод реализует изменение количества товара в корзине
        """
        path = f"{self.base_url}/ajax/basketOrder.php"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Cookie": COOKIE_BASKET
        }
        encoded_body = {
            "data": json.dumps({
                "idCookie": self.id_cookie,
                "idProd": str(self.id_product),
                "type": "plus"
            })
        }
        response_plus = requests.post(path, headers=headers, data=encoded_body)
        print("status:", response_plus.status_code)
        print("text:", response_plus.text)
        return response_plus

    def delete_basket(self) -> requests.Response:
        """ Метод реализует удаление товара из корзины
        """
        path = f"{self.base_url}/ajax/basketOrder.php"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "accept": "application/json",
            "Cookie": COOKIE_BASKET
        }
        encoded_body = {
            "data": json.dumps({
                "idCookie": self.id_cookie,
                "idProd": str(self.id_product),
                "type": "delete"
            })
        }
        response_del = requests.post(path, headers=headers, data=encoded_body)
        print("status:", response_del.status_code)
        print("text:", repr(response_del.text))
        return response_del

    def view_basket(self) -> requests.Response:
        """ Метод реализует просмотр состояния корзины
        """
        path = f"{self.base_url}/ajax/basketList.php"
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": self.base_url,
            "Referer": f"{self.base_url}/",
            "Sec-Ch-Ua": 'Google Chrome";v="137", '
                         '"Chromium";v="137", "Not/A)Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/137.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Cookie": cookie_view
        }
        response_view = requests.post(path, headers=headers)
        print("status:", response_view.status_code)
        print("text:", repr(response_view.text))
        return response_view
