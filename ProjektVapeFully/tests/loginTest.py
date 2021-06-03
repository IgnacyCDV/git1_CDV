import unittest
from BaseTest import BaseTest
from pages.home_page_com import HomePageCom
from pages.loginPageCom import LoginPageCom
valid_name = "marcin"
valid_surname = "Nowak"
valid_gender = "female"
valid_country_code = "+48"
valid_phone_number = "123123123"
valid_email = "kljkjdk@poczta.onet.pl"
invalid_email = "ljkdfdf.pl"
valid_password = "kop"

class RegistrationPageTest(BaseTest):
    """
    Test strony Rejestracji
    """
    def setUp(self):
        print("setUp z RegistrationPageTest")
        super().setUp()
        lpc = LoginPageCom (self.driver)
        lpc._verify_page()



    def test_name_input(self):
        hp = HomePageCom (self.driver)
        hp.click_zaloguj_btn()
        hp.fill_name(valid_name)
        hp.fill_pass(valid_password)
        hp.login_click()
        hp.verify_visible_errors()
        hp.verify_erors(["Unknown username. Check again or try your email address.", "Error: the password you entered for the username " +str(valid_name).lower()+" is incorrect. Lost your password?"])


    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)