import unittest
from BaseTest import BaseTest
from time import sleep
from pages.home_page_com import HomePageCom
from pages.loginPageCom import LoginPageCom
from pages.sign_up_page import SignUpPageCom
valid_name = "marcin"
valid_surname = "Nowak"
valid_gender = "female"
valid_country_code = "+48"
valid_phone_number = "123123123"
valid_email_already_exist= "kljkdk@poczta.onet.pl"
valid_email_working= "Kanalia@poczta.onet.pl"
invalid_email = "ljkdfdf.pl"
valid_password_short = ("kop")
valid_password_correct = ("kop32412321@")
delay = 3

class SignupTest(BaseTest):
    """
    Test strony Rejestracji
    """
    def setUp(self):
        print("setUp z RegistrationPageTest")
        super().setUp()
        lpc = LoginPageCom (self.driver)
        lpc._verify_page()
        hp = HomePageCom(self.driver)
        hp.click_zaloguj_btn()
        hp.sing_up_page_btn()


    def test_name_input(self):
        sup = SignUpPageCom(self.driver)
        sup.fill_email(valid_email_working)
        sup.fill_password(valid_password_correct,delay)
        sleep(2)
        sup.pass_status()
        sup.click_register_btn()
        sup.acc_already_exist_check()

    def tearDown(self):
        self.driver.quit()



if __name__=="__main__":
    unittest.main(verbosity=2)