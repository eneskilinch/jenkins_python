from random import randint
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseClass(object):
    """Base class to initialize the base page that will be called from all pages"""

    ALLOW_OPTIN = (By.CSS_SELECTOR, '#optInText')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, selector):
        """
        Wait for element to present
        :param selector: locator of the element to find

        """
        return self.wait.until(ec.element_to_be_clickable(selector))

    def wait_till_element_disappears(self, selector):
        """
        Wait for element to disappears
        :param selector: locator of the element to find

        """
        return self.wait.until(ec.invisibility_of_element_located(selector))

    def disallow_custom_optin(self):
        """
        Disallows custom optin

        """
        self.wait_for_element(self.ALLOW_OPTIN).click()

    def switch_tab(self, tab_index):
        """
        Switch tab from the current tab
        :param tab_index: index numbers of the selecting tab

        """
        self.driver.switch_to_window(self.driver.window_handles[tab_index])

    def hover(self, selector):
        """
        Hover over the selected element
        :param selector: locator of the element to find

        """
        hover_element = self.wait_for_element(selector)
        hover = ActionChains(self.driver).move_to_element(hover_element)
        hover.perform()

    @staticmethod
    def random_number(first_value, second_value):
        """
        Return random number between parameters
        :param first_value: beginning value of the range
        :param second_value: last value of the range

        """
        return randint(first_value, second_value)

    def element_exists(self, selector, multiple=False):
        """
        Return true if element/elements present and false if element/elements absent
        :param selector: locator of the element to find
        :param multiple: False in default, if True returns the list of WebElements once they are located

        """
        if not multiple:
            try:
                self.wait.until(ec.presence_of_element_located(selector))
                return True
            except TimeoutException:
                return False
        else:
            try:
                self.wait.until(ec.presence_of_all_elements_located(selector))
                return True
            except TimeoutException:
                return False

    def set_cookie(self, name, value):
        """
        Sets a cookie in given variables
        :param name: name of the cookie
        :param value: value of the given cookie name

        """
        cookie = {'name': name, 'value': value, 'path': '/'}
        self.driver.add_cookie(cookie)

    def presence_of_all_elements_located(self, selector):
        """
        Waits until all elements are present on the DOM of a page and visible then returns list of elements
        :param selector: Locator of the desired elements

        """
        return self.wait.until(ec.presence_of_all_elements_located(selector))

    def presence_of_element_located(self, selector):
        """
        Waits until a element i present on the DOM of a page and visible then returns element
        :param selector: Locator of the desired element

        """
        return self.wait.until(ec.presence_of_element_located(selector))
