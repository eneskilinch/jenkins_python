from selenium.webdriver.common.by import By
from base.page_base import BaseClass


class RoyalQueenSeedsLogin:
    """Website login page to user logged in."""

    email = 'loomtestacc@gmail.com'
    password = 'test12345'
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'passwd')
    LOGIN_BUTTON = (By.ID, "SubmitLogin")

    def __init__(self, driver):
        self.driver = driver
        self.methods = BaseClass(self.driver)

    def login(self):
        """
        Fills login informations

        """
        self.methods.wait_for_element(self.EMAIL).send_keys(self.email)
        self.methods.wait_for_element(self.PASSWORD).send_keys(self.password)
        self.methods.wait_for_element(self.LOGIN_BUTTON).click()
