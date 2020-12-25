from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from base.page_base import BaseClass
from time import sleep


class RoyalQueenSeedsMain:
    """RoyalQueenSeedsMain class lands in the website and it has all the navigation functions."""

    website = 'https://www.royalqueenseeds.com/'
    AGE_CONTROL = (By.CSS_SELECTOR, '.button.enter-btn')
    HEADER_LOGIN = (By.XPATH, '//a[@title="Your Account"]')
    LOGIN_BUTTON = (By.XPATH, '//a[@title="Log in"]')
    HOMEPAGE_CONTROL = (By.ID, 'slide-holder')
    HEADER_CATS_CONTAINER = (By.XPATH, '//a[contains(@class, "cat_")]')
    CART_PAGE = (By.XPATH, '//a[contains(@class, "top-cart-checkout")]') # '//*[@title="Check out"]'

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def navigate_to_home_page(self):
        """
        Navigates to the homepage and checks it

        """
        self.driver.get(self.website)
        self.methods.wait_for_element(self.AGE_CONTROL).click()
        home_page_loaded = self.methods.element_exists(self.HOMEPAGE_CONTROL)
        assert home_page_loaded, True

    def navigate_to_login_page(self):
        """
        Navigates to the login page

        """
        try:
            self.methods.wait_for_element(self.HEADER_LOGIN)
            self.methods.hover(self.HEADER_LOGIN)
            self.methods.wait_for_element(self.LOGIN_BUTTON).click()
        except TimeoutException:
            self.methods.hover(self.HEADER_LOGIN)
            self.methods.wait_for_element(self.LOGIN_BUTTON).click()
        sleep(2)

    def navigate_to_random_category_page(self):
        """
        Navigates to a random category page

        """
        sleep(2)
        categories = self.driver.find_elements(*self.HEADER_CATS_CONTAINER)
        random_value = self.methods.random_number(0, len(categories) - 1)
        random_category = categories[random_value]
        random_category.click()

    def navigate_to_cart_page(self):
        """
        Navigates to the cart page

        """
        self.methods.wait_for_element(self.CART_PAGE).click()
