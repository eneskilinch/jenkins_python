from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base.page_base import BaseClass
from time import sleep


class RoyalQueenSeedsCart:
    """Navigating to checkout page and delete items from cart"""

    CHECKOUT_BUTTON = (By.CSS_SELECTOR, '#shoppingCartCheckout')
    DELETE_ITEM = (By.XPATH, '//img[@class= "icon"]')
    EMPTY_CART = (By.ID, 'emptyCartWarning')
    BACK_TO_CART = (By.ID, 'cart-buttons')
    BELOW_MINIMUM_ORDER_AMOUNT = (By.XPATH, '//a[@class="back"][@title= "Previous"]')
    SCROLL_TO_TOP = (By.TAG_NAME, 'body')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def navigate_to_checkout_page(self):
        """
        Navigates the checkout page then come back to the cart page

        """
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        self.methods.wait_for_element(self.CHECKOUT_BUTTON).click()
        if self.methods.element_exists(self.BELOW_MINIMUM_ORDER_AMOUNT):
            try:
                self.methods.wait_for_element(self.BACK_TO_CART).click()
            except TimeoutException:
                self.driver.execute_script("window.history.go(-1)")
        else:
            self.driver.execute_script("window.history.go(-1)")

    def delete_items_from_cart(self):
        """
        Deletes product from the cart page and check if it is any left. If it is exist, deletes that one, too

        """
        while self.methods.presence_of_element_located(self.EMPTY_CART):
            try:
                self.methods.presence_of_element_located(self.DELETE_ITEM).click()
                sleep(2)
            except TimeoutException:
                break
        assert self.methods.presence_of_element_located(self.EMPTY_CART).is_displayed
