


# Задача
# Напиши функцию, которая принимает на вход строку и возвращает её перевёрнутый вариант.
# Запрещается использовать [::-1]


def reverse_str(row: str) -> str:
    ...




if __name__ == '__main__':
    assert reverse_str('hello') == 'olleh'
    assert reverse_str('world') == 'dlrow'
    assert reverse_str('') == ''


# ---------------------------------------


# Задача
# Напишите функцию, которая принимает список и целое число
# Функция возвращает количество вхождений числа в списке.


def count_in_list(row: list, digit: int) -> int:
    ...


if __name__ == '__main__':
    assert count_in_list([1, 2, 3, 4, 5], 2) == 1
    assert count_in_list([1, 3, 3], 3) == 2
    assert count_in_list([1, 10, 9, 8, 0], 4) == 0

# ---------------------------------------



# Задача
# Напиши функцию которая возвращает только четные числа из списка.


def filter_even_numbers(number: list) -> list:
    ...


if __name__ == '__main__':
    assert filter_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_even_numbers([1, 3, 5]) == []
    assert filter_even_numbers([2]) == [2]
    assert filter_even_numbers([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]
    assert filter_even_numbers([1, 1, 1, 1, 1]) == []

# ---------------------------------------

# Задача
#  Реализуй функцию, которая проверяет, является ли строка палиндромом.
#  Прротестируй ее.

def is_palindrome(s: str) -> bool:
    ...

if __name__ == '__main__':
    assert is_palindrome('aba') == True
    assert is_palindrome('sddf') == False


# ---------------------------------------


# Задача
# Создать фикстуру для имитации подключения к базе данных
# которая закрывается после выполнения теста.

class Database:
    def connect(self):
        print("Database connected")
        return self

    def close(self):
        print("Database closed")

...

# Фикстура для базы данных.
# @pytest.fixture
# def db():
#     db = Database().connect()
#     yield db
#     db.close()
#
# # Пример задачи:
# # Напишите тесты, использующие фикстуру `db`.
# def test_db_connection(db):
#     assert db is not None


# ---------------------------------------
# Задача
# Что выведется на экран при запуске тестов?


def foo():
    row = "" * 10
    return row

@pytest.fixture
def foo_fixture():
    return foo()


def test_foo(foo_fixture):
    assert foo_fixture


# ---------------------------------------
# Что будет выведено на экран при запуске тестов?
# В каком порядке выполняются вызовы функций и фикстур?

import pytest


def foo():
    print("foo")


@pytest.fixture(scope="function")
def function_one():
    yield foo
    print('Fixture one')


@pytest.fixture(scope="session")
def function_two(function_one):
    print('Fixture two')
    yield function_one


def test_anything(function_two):
    print('CODE')

# ---------------------------------------
# Задача
# Дан отсортированный массив чисел.
# Нужно вернуть отсортированный массив квадратов этих чисел.


# Пример:
# Input: nums = [1,  2, 5]
# Output: squares = [1, 4, 25]


# ---------------------------------------
import pytest

from Assets.users import *
from Pages.DraftPage import DraftPage
from api_client import Client
from Pages.LoginPage import *
from Pages.CartPage import *
from Pages.StockPage import *
from Locators.CartLocatorts import Order
from Locators.LoginPage import *
import time
import datetime
from plugin import xray

client = Client("https://www.citilink.ru/")
CART = 'api/v2/cart'
CART_ID = 'api/v2/cart/{}'


@pytest.mark.usefixtures("driver")
class Testclass:

    # QA-1
    @xray("QA-1")
    @pytest.mark.regress
    def test_move_draft_to_cart_with_saving(self, driver):
        # название черновика
        draft_name = "autotest_" + str(datetime.datetime.now())
        # список номенклатуры для добавления в черновик
        list = """1128418
            1622267
            1470855"""

        login_page = LoginPage(driver)
        cart_page = CartPage(driver)
        stock_page = StockPage(driver)
        draft_page = DraftPage(driver)
        # логинимся
        login_page.login(user.name, user.password)
        login_page.wait_until_element_visible(Login.logout)
        # переходим на стр Корзина
        login_page.navigate_to_page("shoppingcart")
        # очищаем корзину
        cart_page.clear_cart_on_cart_page()
        # добавляем списком товары в корзину
        cart_page.load_list(list)
        # порверяем, что все товары успешно подъехали в окне загрузки
        cart_page.check_list_NN(list)
        cart_page.wait_and_click(Order.load_list_confirm)
        # проверяем, что все товы успешно добавились в корзину
        cart_page.check_table_NN(list)
        # увеличиваем кол-во товара
        stock_page.add_item_by_increment("1622267", 4)
        stock_page.add_item_by_increment("1470855", 9)
        time.sleep(1)  # добавлен таймслип, так как иначе не все товары успевают добавиться в корзину перед созданием черновика и остаются в корзине после созжания черновика
        # нажимаем кнопку Сохранить черновик и добавляем коммент и пометки
        cart_page.add_to_draft(draft_name, ("comment " + draft_name), ("notes " + draft_name))
        # создаем черновик
        cart_page.wait_and_click((By.XPATH, "//a[text()='{}']".format(draft_name)))
        # проверяем, что название, комментарий и пометки к черновику
        cart_page.check_draft_fields(draft_name, ("comment " + draft_name), ("notes " + draft_name))
        # проверяем, что в черновик успешно добавились товары
        cart_page.check_table_NN(list)

        # переносим черновик в корзину
        draft_page.move_to_cart_button(draft_saving=True)

        # проверяем, что все товары успешно подъехали  в корзину
        cart_page.check_table_NN(list)
        # проверяем, что остальные данные - наименование, пометки, комментарий успешно подъехали
        cart_page.check_name_comment_notes(order_name=draft_name, order_comment="comment " + draft_name, order_userComment="notes " + draft_name)
        # переходим на стр Черновики
        login_page.navigate_to_page("drafts")
        # проверяем, что в списке черновиков отображается ранее созданный черновик
        draft_page.find_first_draft_and_check_name(draft_name, state=True)

# ---------------------------------------
# Задача
# Что выведется на экран?
c = [5]
a = [c]
b = a * 3
b[0] += [4]
print(b)


# ---------------------------------------
# Задача
# Отсортируй список по количеству по убыванию.


a = [ {'name': 'cpu', 'quantity': 1}, {'name': 'ram', 'quantity': 4}, {'name': 'ssd', 'quantity': 2}]

# ---------------------------------------
# Задача
# Создай новый список только с нечетными числами.

row = [1, 2, 3, 4, 5]


# ---------------------------------------
# Задача
# Что выведется на экран?


def extend_list(value, list=[]):
   list.append(value)
   return list

a = extend_list(10)
b = extend_list(123, [])
c = extend_list('a')

print(a)
print(b)
print(c)


