from selenium.webdriver.common.by import By
from base.page_base import BaseClass
from time import sleep


class RoyalQueenSeedsProduct:
    """Product page to select size and add to cart."""

    NUMBER_SEEDS_CONTAINER = (By.CSS_SELECTOR, '.attributes-block')
    ADD_TO_CART = (By.CSS_SELECTOR, '#add_to_cart')
    ADDED_TO_CART = (By.ID, 'cart_block_total')
    PRODUCT_STOCK = (By.ID, 'availability_value')
    POPUP_CLOSE_BUTTON = (By.XPATH, '')
    OUT_OF_STOCK = (By.CSS_SELECTOR, '#availability_value')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    # def select_size(self):
    #     """
    #     Selects product size
    #
    #     """
    #     if self.methods.element_exists(self.NONE_SIZE):
    #         self.methods.wait_for_element(self.AVAILABLE_SIZE).click()

    def check_stock_info(self):
        """
         Search for stock info if the product is not in stock returns False

         """
        availability = self.methods.presence_of_element_located(self.OUT_OF_STOCK).text
        if availability.lower() != 'no stock':
            return True
        else:
            return False

    def add_product_to_cart(self):
        """
        Adds product to the cart page and check is it added successfully

        """
        sleep(1)
        cart_total = self.methods.presence_of_element_located(self.ADDED_TO_CART).text
        self.methods.wait_for_element(self.ADD_TO_CART).click()
        if self.methods.element_exists(self.ADDED_TO_CART):
            try:
                sleep(1)
                successfully_added = self.methods.presence_of_element_located(self.ADDED_TO_CART).text
                assert cart_total != successfully_added  # change assertion if any bug appears
            except AssertionError:
                self.add_product_to_cart()
        else:
            self.add_product_to_cart()
