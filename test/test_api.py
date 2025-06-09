import pytest
import allure
import logging
logging.basicConfig(level=logging.DEBUG)

from class_basketAPI import BasketApi

@pytest.mark.api
@allure.id("Api-1")
@allure.severity("critical")
@allure.title("Добавление товара в корзину")
@allure.feature("API. Добавление товара")
@allure.description("API тестирование.Добавление товара в корзину")
def test_post_basket_add():
    with allure.step("Отправляем POST запрос. Добавление товара в корзину"):
        basket_api = BasketApi()
        response = basket_api.add_basket()

    print(f"Полный ответ: {response}")  # Выведите полный ответ
    with allure.step("Ожидаем статус == 200"):
        assert response.status_code == 200

    # assert "1" in response.text.strip, \
    #     f"Ожидалось увидеть '1' в ответе, получено: {response.text}"


@pytest.mark.api
@allure.id("Api-2")
@allure.severity("medium")
@allure.title("Изменение количества товара в корзине")
@allure.feature("API. Изменение количества товара")
@allure.description("API тестирование.Изменение количества товара в корзине")
def test_post_basket_plus():
    basket_api = BasketApi()
    with allure.step("Отправляем POST запрос. Изменение количества товара в корзине"):
        response_plus = basket_api.plus_basket()

    print(f"Полный ответ: {response_plus}")  # Выведите полный ответ
    with allure.step("Ожидаем статус == 200"):
        assert response_plus.status_code == 200

    # with allure.step("Проверить количество товара в ответе от сервера"):
    #     assert "2" in response_plus.text, f"Количество товара не равно {2}"



@pytest.mark.api
@allure.id("Api-3")
@allure.severity("medium")
@allure.title("Удаление товара из корзины")
@allure.feature("API. Удаление товара")
@allure.description("API тестирование.Удаление товара из корзины")
def test_post_basket_delete():
    basket_api = BasketApi()
    with allure.step("Отправляем POST запрос. Удаление товара из корзины"):
        response_del = basket_api.delete_basket()

    print(f"Полный ответ: {response_del}")  # Выведите полный ответ
    with allure.step("Ожидаем статус == 200"):
        assert response_del.status_code == 200


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

    print(f"Полный ответ: {view_basket.text}")  # Выведите полный ответ
    with allure.step("Ожидаем статус == 200"):
        assert view_basket.status_code == 200

    with allure.step("Проверить ответ от сервера"):
        expected_message = "\n<h2>Корзина пуста, необходимо это исправить</h2>\n\n\n\n\n"
        actual_response = view_basket.text.strip()  # Убираем лишние пробелы и переводы строк
        assert expected_message.strip() in actual_response, f"Ответ от сервера неверный: {actual_response}"