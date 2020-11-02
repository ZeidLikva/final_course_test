from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('n', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, n):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_basket_message()
    page.is_right_product()
    page.should_be_basket_price()
    page.is_right_price()
