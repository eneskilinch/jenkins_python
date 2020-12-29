from random import choice
from selenium.webdriver.common.by import By
from base.page_base import BaseClass


class RoyalQueenSeedsCategory:
    """RoyalQueenSeedsCategory is selecting one random product from category page."""

    PRODUCTS_LIST = (By.CSS_SELECTOR, '.product-image-link.product_img_link')
    COOKIE_BUTTON = (By.CSS_SELECTOR, '.cookie-popup__accept')

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def accept_cookies(self):
        """
        Clicks accept cookies button

        """
        self.methods.wait_for_element(self.COOKIE_BUTTON).click()

    def click_random_product(self):
        """
        Clicks random product from the category page

        """
        products = self.methods.presence_of_all_elements_located(self.PRODUCTS_LIST)
        try:
            choice(products).click()
        except:
            self.click_random_product()
