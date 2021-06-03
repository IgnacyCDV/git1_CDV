
from BaseTest import BaseTest
from time import sleep
from pages.product_page import ProductPage
from pages.loginPageCom import LoginPageCom
from pages.cart_page import CartPage
product_SKU = "100156"
variant = "Onyx (basic set)"
variant2 = "Burgundy (complete set)"
variant3 = "Sage (basic set)"

class SignupTest(BaseTest):
    """
    Test strony Rejestracji
    """
    def setUp(self):
        print("setUp z RegistrationPageTest")
        super().setUp()
        lpc = LoginPageCom (self.driver)
        lpc._verify_page()
        pp = ProductPage(self.driver)

        pp.product_search(product_SKU)
        pp.variable_product_choose(variant2)
        sleep(3)
        pp.add_to_basket()
        pp.go_to_cart()



    def test_name_input(self):
        cp = CartPage(self.driver)
        cp.free_courier(variant2)
        cp.go_to_chekout()
        sleep(5)



    def tearDown(self):
        self.driver.quit()



if __name__=="__main__":
    unittest.main(verbosity=2)