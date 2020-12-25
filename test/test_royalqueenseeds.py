import unittest
from selenium import webdriver
from base.page_base import BaseClass
from page.cart_page import RoyalQueenSeedsCart
from page.category_page import RoyalQueenSeedsCategory
from page.login_page import RoyalQueenSeedsLogin
from page.main_page import RoyalQueenSeedsMain
from page.product_page import RoyalQueenSeedsProduct


class RoyalQueenSeedsHappyPath(unittest.TestCase):
    """Test case is:
      1. Go to given website
      2. Click login page button
      3. Try to logged in
      4. Go to random category page
      5. Select one random product
      6. Select product size
      7. Add product to cart
      8. Go to cart page
      9. Go to checkout page
      10. Delete items from cart and tear down
      """

    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('--disable-notifications')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.maximize_window()
        self.methods = BaseClass(self.driver)
        self.royalqueenseeds_main_page = RoyalQueenSeedsMain(self.driver)
        self.royalqueenseeds_login_page = RoyalQueenSeedsLogin(self.driver)
        self.royalqueenseeds_category_page = RoyalQueenSeedsCategory(self.driver)
        self.royalqueenseeds_product_page = RoyalQueenSeedsProduct(self.driver)
        self.royalqueenseeds_cart_page = RoyalQueenSeedsCart(self.driver)

    def test_royalqueenseeds(self):
        self.royalqueenseeds_main_page.navigate_to_home_page()
        self.royalqueenseeds_main_page.navigate_to_login_page()
        self.royalqueenseeds_login_page.login()
        self.royalqueenseeds_main_page.navigate_to_random_category_page()
        self.royalqueenseeds_category_page.accept_cookies()
        self.royalqueenseeds_category_page.click_random_product()
        while not self.royalqueenseeds_product_page.check_stock_info():
            self.royalqueenseeds_main_page.navigate_to_random_category_page()
            self.royalqueenseeds_category_page.click_random_product()
        self.royalqueenseeds_product_page.add_product_to_cart()
        self.royalqueenseeds_main_page.navigate_to_cart_page()
        self.royalqueenseeds_cart_page.navigate_to_checkout_page()
        self.royalqueenseeds_cart_page.delete_items_from_cart()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
