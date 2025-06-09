import pytest
import allure

from constants import *

@pytest.mark.ui
@allure.id("MainPage-1")
@allure.severity("blocker")
@allure.title("Переход в корзину")
@allure.story("Переход с главной страницы в корзину")
@allure.feature("кнопка 'корзина'")
@allure.description("Функциональность кнопки 'корзина' на главной странице")
def test_open_basket(main_page):
    with allure.step("Нажать на кнопку 'корзина'"):
        main_page.open_basket()

    with allure.step("Подождать появления модального окна корзины"):
        try:
            basket_modal = main_page.basket_modal()
            assert basket_modal.is_displayed(), "Модальное окно корзины не появилось"
        except TimeoutException as e:
            raise AssertionError(f"Тайм-аут ожидания появления модального окна корзины: {e}")


@pytest.mark.ui
@allure.id("MainPage-2")
@allure.severity("Critical")
@allure.title("Добавить продукт")
@allure.story("Добавить продукт в корзину")
@allure.feature("Кнопка 'В корзину'")
@allure.description("Добавление продукта в корзину c главной страницы, нажав кнопку 'В корзину'")
def test_products(main_page):
    with allure.step("Добавить продукт, нажав кнопку 'В корзину'"):
        main_page.add_to_basket()
    with allure.step("Открыть корзину и убедиться, что количество добавленного товара = 1 шт"):
        main_page.open_basket()
        basket_count = main_page.check_quantity_to_basket()

    expected_quantity = "1 шт"
    with allure.step("Проверить фактическое количество товаров в корзине (basket_count) "
                     "с ожидаемым количеством (expected_quantity)"):
        assert basket_count == expected_quantity, (
            f"Количество товаров в корзине отличается от ожидаемого ({expected_quantity}). "
            f"Фактическое количество: {basket_count}")


@pytest.mark.ui
@allure.id("MainPage-3")
@allure.severity("blocker")
@allure.title("Заполнение формы отправки")
@allure.story("Заполнение формы отправки данными пользователя")
@allure.feature("Форма отправки данных")
@allure.description("Функциональность формы заполнения данных пользователя в корзине")
def test_input(main_page):
    with allure.step("Добавить продукт, нажав кнопку 'В корзину'"):
        main_page.add_to_basket()
    with allure.step("Нажать на кнопку 'корзина'"):
        main_page.open_basket()
    with allure.step("Ввести имя и номер телефона пользователя"):
        name_and_phone = main_page.input_text(NAME_ANY, PHONE_NUMBER)
    with allure.step("Нажать кнопку 'Отправить'"):
        main_page.button_send()

    expected = NAME_ANY, PHONE_NUMBER
    with allure.step("Проверить соответствие введенных данных пользователя с ожидаемым результатом"):
        assert name_and_phone == expected, (
            f"Введенные данные отличаются от ожидаемого результата ({expected}). "
            f"Фактическое имя и номер телефона: {name_and_phone}")


@pytest.mark.ui
@allure.id("MainPage-4")
@allure.severity("Minor")
@allure.title("Переход в раздел продукция")
@allure.story("Переход с главной страницы в раздел продукция")
@allure.feature("раздел 'Продукция'")
@allure.description("Функциональность кнопки 'Продукция' на главной странице")
def test_products(main_page):
    with allure.step("Нажать на кнопку 'продукция'"):
        main_page.click_products()

    with allure.step("Подождать появления блока 'Наша продукция'"):
        try:
            blok_products = main_page.blok_products()
            assert blok_products.is_displayed(), f"Блок 'Наша продукция' не появился"
        except TimeoutException as e:
            raise AssertionError(f"Тайм-аут ожидания появления блока 'Наша продукция': {e}")


@pytest.mark.ui
@allure.id("MainPage-5")
@allure.severity("Minor")
@allure.title("Кнопка возврата Наверх")
@allure.story("Возврат с нижней части страницы вверх, нажав на появляющуюся кнопку 'Наверх'")
@allure.feature("кнопка Наверх")
@allure.description("Функциональность кнопки 'Наверх' на главной странице")
def test_click_up(main_page):
    with allure.step("Нажать на кнопку 'Наверх'"):
        main_page.click_up()

    with allure.step("Подождать появления блока header"):
        try:
            block_header = main_page.block_header()
            assert block_header.is_displayed(), f"Блок header не появился"
        except TimeoutException as e:
            raise AssertionError(f"Тайм-аут ожидания появления блока header: {e}")