import pytest
import allure
import logging

from class_basketAPI import BasketApi
from constants import ID_PRODUCT

logging.basicConfig(level=logging.DEBUG)


@pytest.mark.api
@allure.id("Api-1")
@allure.severity("critical")
@allure.title("Добавление товара в корзину")
@allure.feature("API. Добавление товара")
@allure.description("API тестирование."
                    "Очистить корзину и добить товар в корзину")
def test_post_basket_add():
    basket_api = BasketApi()

    with allure.step("Отправляем POST запрос. Удаление товара в корзине"):
        basket_api.delete_basket()
    with allure.step(f"Отправляем POST запрос. "
                     f"Добавление товара id=f'{ID_PRODUCT}' - 1 шт в корзину"):
        response = basket_api.add_basket()

        print(f"Полный ответ: {response.text}")   # Выведите полный ответ
    with allure.step("Ожидаем статус == 200"):
        assert response.status_code == 200, f"Получили статус {response.status_code}, ожидали 200."
    with allure.step("Проверить количество товара в ответе от сервера"):
        expected_content = "1"
        assert expected_content in response.text, \
            f"Ожидалось увидеть '{expected_content}' в ответе, получено: {response.text}"


@pytest.mark.api
@allure.id("Api-2")
@allure.severity("medium")
@allure.title("Изменение количества товара в корзине")
@allure.feature("API. Изменение количества товара")
@allure.description("API тестирование.Очистить корзину, "
                    "добить товар в корзину и изменить количества товара в корзине")
def test_post_basket_plus():
    basket_api = BasketApi()

    with allure.step("Отправляем POST запрос. Удаление товара в корзине"):
        basket_api.delete_basket()
    with allure.step(f"Отправляем POST запрос. Добавление товара id=f'{ID_PRODUCT}' - 1 шт в корзину"):
        basket_api.add_basket()
    with allure.step(f"Отправляем POST запрос. Изменение количества товара id=f'{ID_PRODUCT}' в корзине"):
        response_plus = basket_api.plus_basket()
    with allure.step("Отправляем POST запрос. Просмотр корзины"):
        basket_api.view_basket()

    with allure.step("Ожидаем статус == 200"):
        assert response_plus.status_code == 200
    with allure.step("Проверить количество товара в ответе от сервера"):
        assert "2" in response_plus.text, f"Количество товара не равно {2}"


@pytest.mark.api
@allure.id("Api-3")
@allure.severity("medium")
@allure.title("Удаление товара из корзины")
@allure.feature("API. Удаление товара")
@allure.description("API тестирование.Удалить товар из корзины и проверить состояние корзины")
def test_post_basket_delete():
    basket_api = BasketApi()
    with allure.step("Отправляем POST запрос. Удаление товара из корзины"):
        response_del = basket_api.delete_basket()
    with allure.step("Отправляем POST запрос. Просмотр корзины"):
        basket_api.view_basket()

    print(f"Полный ответ: {response_del.text}")  # Выведите полный ответ
    with allure.step("Ожидаем статус == 200"):
        assert response_del.status_code == 200
    with allure.step("Проверить количество товара в ответе от сервера"):
        assert "0" in response_del.text, f"Количество товара не равно {0}"


@pytest.mark.api
@allure.id("Api-4")
@allure.severity("medium")
@allure.title("Просмотр корзины")
@allure.feature("API. Просмотр состояния корзины")
@allure.description("API тестирование.Просмотр состояния корзины")
def test_post_basket_view():
    basket_api = BasketApi()
    with allure.step("Отправляем POST запрос. Просмотр корзины"):
        view_basket = basket_api.view_basket()

    with allure.step("Ожидаем статус == 200"):
        assert view_basket.status_code == 200
    with allure.step("Проверить ответ от сервера"):
        assert view_basket.text
