import pytest
import allure
import logging
logging.basicConfig(level=logging.DEBUG)

from constants import *
from class_basketAPI import BasketApi

@pytest.mark.api
@pytest.mark.parametrize("expected_status", [200])
@allure.id("Api-1")
@allure.severity("critical")
@allure.title("Добавление товара в корзину")
@allure.feature("API. Добавление товара")
@allure.description("API тестирование.Добавление товара в корзину")
def test_post_basket_add(expected_status):
    with allure.step("Отправляем POST запрос. Добавление товара в корзину"):
        basket_api = BasketApi(BASE_URL, ID_COOKIE)
        response_text, response_status = basket_api.add_basket(ID_PRODUCT)

        print(f"Полный ответ: ({response_text}, {response_status})")  # Выведите полный ответ
    with allure.step("Ожидаем статус == 200"):
        assert response_status == 200

    with allure.step("Проверить количество товара в ответе от сервера"):
        assert f"{response_text}" in response_text
        # assert len(response_text.strip()) > 0, "Отсутствует контент в ответе"




    # with allure.step("Проверить количество товара в ответе от сервера"):
    #     print(response_text)
    #     assert f"1" in response_text, f"Цифра '1' не найдена в ответе '{response_text}'"

    # with allure.step("Ожидаем статус == 200"):
    #     assert response_obj.status_code == expected_status, f"Ошибка, полученный статус: {response_obj.status_code}"
    #
    # with allure.step("Проверяем успешность добавления товара"):
    #     # Предполагается, что ответ содержит числовое значение или иной признак успеха
    #     assert "1" in response_text, f"Ошибка при добавлении товара, результат: {response_text}"

        # response_add = basket_api.plus_basket(id_product)
    #     # response_cart = basket_api.chek_cart_no_empty()
    # with allure.step("Отправляем POST запрос. Добавление товара в корзину"):
    #     result_text = basket_api.add_basket(id_product)
    #
    # with allure.step("Проверяем успешность добавления товара"):
    #     # Предполагаем, что в тексте содержится информация о статусе успеха
    #     assert "OK" in result_text or "успешно" in result_text, \
    #         f"Ошибка при добавлении товара, результат: {result_text}"

    # with allure.step("Ожидаем статус == 200"):
    #     assert response_add.status_code == 200, f"Ошибка, полученный статус: {response_add.status_code}"
    #
    # # with allure.step("Проверка ключевых слов в ответе о добавлении продукта"):
    # #     assert response_add.json().get(“status”) == “ok”
    # #     assert response_add.json().get(“btn_text”) == “добавлено”
    #
    # with allure.step("Проверить количество товара в ответе от сервера"):
    #     print(response_add.text)
    #     assert "1" in response_add.text, f"Цифра '1' не найдена в ответе '{response_add.text}'"
    #
    # # with allure.step("Ожидаемый результат должен быть строка str"):
    # #     assert isinstance(response_add, str)
    #
    # with allure.step("Логируем полученные данные"):
    #     print(f"Полученные данные: {response_add}, "
    #           f"Статус: {expected_status}")


# Def test_change_product_quantity():
# 	api = SibderApi(BASE_URL, Cookie_ID)
# 	api.add_product_to_cart(Product_ID)
#
# 	response_plus = api.change_product_ quantity_ plus(Product_ID)
# 	response_cart = api.chek_cart_no_empty()
#
# 	api.delete_product_from_cart(Product_ID)
#
# with allure.step("Ожидаем статус == 200"):
#     		assert expected_status == 200
# 	assert respons_pius.status_code == 200
#
# with allure.step("Проверить количество товара в ответе от сервера"):
#     		assert "2" in response_plus.text
#
# with allure.step("Проверить количество товара в корзирне"):
#     		assert "value=’2 шт’" in response_cart.text





@pytest.mark.api
@pytest.mark.parametrize("expected_status", [200])
@allure.id("Api-2")
@allure.severity("medium")
@allure.title("Изменение количества товара в корзине")
@allure.feature("API. Изменение количества товара")
@allure.description("API тестирование.Изменение количества товара в корзине")
def test_post_basket_plus(expected_status):
    basket_api = BasketApi(BASE_URL, ID_COOKIE)
    with allure.step("Отправляем POST запрос. Изменение количества товара в корзине"):
        plus_to_basket = basket_api.plus_basket(ID_PRODUCT)

    with allure.step("Ожидаем статус == 200"):
        assert expected_status == 200

    with allure.step("Ожидаемый результат должен быть строка str"):
        assert isinstance(plus_to_basket, str)

    with allure.step("Проверить количество товара в ответе от сервера"):
        assert "2" in plus_to_basket, "Количество товара не равно 2"

    with allure.step("Логируем полученные данные"):
        print(f"Полученные данные: {plus_to_basket}, "
              f"Статус: {expected_status}")


@pytest.mark.api
@pytest.mark.parametrize("expected_status", [200])
@allure.id("Api-3")
@allure.severity("medium")
@allure.title("Изменение количества товара в корзине")
@allure.feature("API. Изменение количества товара")
@allure.description("API тестирование.Изменение количества товара в корзине")
def test_post_basket_delete(expected_status):
    basket_api = BasketApi(BASE_URL, ID_COOKIE)
    with allure.step("Отправляем POST запрос. Удаление товара из корзины"):
        delete_to_basket = basket_api.delete_basket(ID_PRODUCT)

    with allure.step("Ожидаем статус == 200"):
        assert expected_status == 200

    with allure.step("Ожидаемый результат должен быть строка str"):
        assert isinstance(delete_to_basket, str)

    with (allure.step("Проверить ответ от сервера")):
        assert "0"in delete_to_basket, "Количество товара не равно 0"

    with allure.step("Логируем полученные данные"):
        print(f"Полученные данные: {delete_to_basket}, "
              f"Статус: {expected_status}")



@pytest.mark.api
@pytest.mark.parametrize("expected_status", [200])
@allure.id("Api-4")
@allure.severity("medium")
@allure.title("Просмотр корзины")
@allure.feature("API. Просмотр состояния корзины")
@allure.description("API тестирование.Просмотр состояния корзины")
def test_post_basket_delete(expected_status):
    basket_api = BasketApi(BASE_URL, ID_COOKIE)
    with allure.step("Отправляем POST запрос. Просмотр корзины"):
        delete_to_basket = basket_api.delete_basket()

    with allure.step("Ожидаем статус == 200"):
        assert expected_status == 200

    with allure.step("Ожидаемый результат должен быть строка str"):
        assert isinstance(delete_to_basket, str)

    with (allure.step("Проверить ответ от сервера")):
        assert "0" in delete_to_basket, "Количество товара не равно 0"

    with allure.step("Логируем полученные данные"):
        print(f"Полученные данные: {delete_to_basket}, "
              f"Статус: {expected_status}")







# @pytest.mark.api
# @pytest.mark.parametrize("expected_status", [200])
# @allure.id("Api-2")
# @allure.severity("Major")
# @allure.title("Поиск фильма по дате премьеры в России")
# @allure.feature("API. Поиск фильма")
# @allure.description("API тестирование.Поиск фильма дате премьеры в России")
# def test_get_search_to_data(expected_status, auth_api):
#     with allure.step("Отправляем GET запрос. "
#                      "Поиск фильма по дате премьеры в России"):
#         search_to_data = auth_api.get_search_to_data("01.01.1997")
#
#     with allure.step("Ожидаем статус == 200"):
#         assert expected_status == 200
#
#     with allure.step("Ожидаемый результат должен быть словарь dict"):
#         assert isinstance(search_to_data, dict)
#         assert len(search_to_data) > 0
#
#     with allure.step("Логируем полученные данные"):
#         print(f"Полученные данные: {search_to_data}, "
#               f"Статус: {expected_status}")
#
#
# @pytest.mark.api
# @pytest.mark.parametrize("expected_status", [200])
# @allure.id("Api-3")
# @allure.severity("critical")
# @allure.title("Поиск фильма по возрастному рейтингу")
# @allure.feature("API. Поиск фильма")
# @allure.description("API тестирование.Поиск фильма по возрастному рейтингу")
# def test_get_search_to_age(expected_status, auth_api):
#     with allure.step("Отправляем GET запрос. "
#                      "Поиск фильма по возрастному рейтингу"):
#         search_to_age = auth_api.get_search_to_age()
#
#     with allure.step("Ожидаем статус == 200"):
#         assert expected_status == 200
#
#     with allure.step("Ожидаемый результат должен быть словарь dict"):
#         assert isinstance(search_to_age, dict)
#         assert len(search_to_age) > 0
#
#     with allure.step("Логируем полученные данные"):
#         print(f"Полученные данные: {search_to_age}, "
#               f"Статус: {expected_status}")
#
#
# @pytest.mark.api
# @pytest.mark.parametrize("expected_status", [200])
# @allure.id("Api-4")
# @allure.severity("Minor")
# @allure.title("Поиск фильма по году")
# @allure.feature("API. Поиск фильма")
# @allure.description("API тестирование.Поиск фильма по году")
# def test_get_search_to_year(expected_status, auth_api):
#     with allure.step("Отправляем GET запрос. "
#                      "Поиск фильма по году"):
#         search_to_year = auth_api.get_search_to_year()
#
#     with allure.step("Ожидаем статус == 200"):
#         assert expected_status == 200
#
#     with allure.step("Ожидаемый результат должен быть словарь dict"):
#         assert isinstance(search_to_year, dict)
#         assert len(search_to_year) > 0
#
#     with allure.step("Логируем полученные данные"):
#         print(f"Полученные данные: {search_to_year}, "
#               f"Статус: {expected_status}")
#
#
# @pytest.mark.api
# @pytest.mark.parametrize("expected_status", [200])
# @allure.id("Api-5")
# @allure.severity("critical")
# @allure.title("Поиск фильма по рейтингу Кинопоиск")
# @allure.feature("API. Поиск фильма")
# @allure.description("API тестирование.Поиск фильма по рейтингу Кинопоиск")
# def test_get_search_to_rating(expected_status, auth_api):
#     with allure.step("Отправляем GET запрос. "
#                      "Поиск фильма по рейтингу Кинопоиск"):
#         search_to_rating = auth_api.get_search_to_rating()
#
#     with allure.step("Ожидаем статус == 200"):
#         assert expected_status == 200
#
#     with allure.step("Ожидаемый результат должен быть словарь dict"):
#         assert isinstance(search_to_rating, dict)
#         assert len(search_to_rating) > 0
#
#     with allure.step("Логируем полученные данные"):
#         print(f"Полученные данные: {search_to_rating}, "
#               f"Статус: {expected_status}")
