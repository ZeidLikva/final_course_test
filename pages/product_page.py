from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def should_be_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_MESSAGE), "Нет сообщения о добавлении товара в корзину"

    def should_be_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), "Нет сообщения со стоимостью корзины"
    def is_right_product(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_message = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text
        assert product_name == basket_message, "Товар не добавлен в корзину"

    def is_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, "Неверная цена товара"