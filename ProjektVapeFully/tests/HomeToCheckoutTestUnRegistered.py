from BaseTest import BaseTest
from time import sleep
from pages.product_page import ProductPage
from pages.loginPageCom import LoginPageCom
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage
product_SKU = "100156"
variant = "Onyx (basic set)"
variant2 = "Burgundy (complete set)"
variant3 = "Sage (basic set)"
email ="jakismasil@gmail.com"

valid_name = "marcin"
valid_surname = "Nowak"
valid_gender = "female"
valid_postcode = "78-100"
valid_phone_number = "602304956"
valid_email = "kljkjdk@poczta.onet.pl"
valid_country = "poland"
valid_address ="kolano 12"
valid_city = "Kołobrzeg"
deley =0.5
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
        cp = CartPage(self.driver)
        cp.free_courier(variant2)
        cp.go_to_chekout()



    def test_name_input(self):
        chp = CheckOutPage(self.driver)
        chp.form_check_email(email, deley)
        chp.form_check_name(valid_name)
        chp.form_check_lastname(valid_surname)
        chp.form_check_country(valid_country)
        chp.form_check_address(valid_address)
        chp.form_check_postcode(valid_postcode)
        chp.form_check_city(valid_city)
        chp.form_check_phone(valid_phone_number)
        chp.click_outside()
        sleep(5)
        chp.form_check_ihaveread()
        chp.click_outside()
        sleep(5)
        chp.from_check_placeorder()

        sleep(5)
        chp.check_URL()






    def tearDown(self):
        self.driver.quit()



if __name__=="__main__":
    unittest.main(verbosity=2)