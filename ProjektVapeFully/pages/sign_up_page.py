
from time import sleep
from locatorsy import SignUpPage
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpPageCom(BasePage):
    """
    Strona logowania
    """
    def fill_email(self, email):
        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.element_to_be_clickable(SignUpPage.SUP_EMAIL))

        element.send_keys(email)

    def fill_password(self, password, deley):
        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.element_to_be_clickable(SignUpPage.SUP_PASS))
        # element = self.driver.find_element(*HomePage.INPUT_NAME_BP)
        for c in password:
            element.send_keys(c)
            sleep(deley)
        #element.send_keys(Keys.ENTER)
    def click_register_btn(self):
        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.element_to_be_clickable(SignUpPage.SUP_REG_BTN))
        element.click()
    def not_click_register_btn_(self):
        self.driver.find_element(*SignUpPage.SUP_REG_BTN_DISABLED)

    def pass_status(self):
        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.presence_of_element_located(SignUpPage.PASSWORD_STRENGHT))
        str =  element.text
        print(str)

    def acc_already_exist_check(self):
        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.presence_of_element_located(SignUpPage.ERROR_ALREADY_EXIST))
        err_text = element.text
        assert err_text == "Error: An account is already registered with your email address. Please log in."