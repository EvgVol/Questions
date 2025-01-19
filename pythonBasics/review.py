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
