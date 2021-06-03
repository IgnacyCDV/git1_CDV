from pages.base_page import BasePage
from locatorsy import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePageCom(BasePage):
    """
    Strona domowa
    """
    def click_zaloguj_btn(self):
        # Tworzenie instancji klasy WebDriverWait
        wait = WebDriverWait(self.driver, 60)
        # Wywołanie metody until na obiekcie WebDriverWait
        # W efekcie otrzymamy element (jeśli warunek wystąpi)
        element = wait.until(EC.element_to_be_clickable(HomePage.MY_ACCOUNT_BTN_COM))
        element.click()



        # Wpisanie imienia
    def fill_name(self, name):
        # Wyszukac input imienia
        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.element_to_be_clickable(HomePage.INPUT_NAME_BP))
        # element = self.driver.find_element(*HomePage.INPUT_NAME_BP)
        element.send_keys(name)


    def fill_pass(self, password):
        element = self.driver.find_element(*HomePage.IMPUT_PASS_BP)
        element.send_keys(password)
    def login_click(self):
        element = self.driver.find_element(*HomePage.SIGN_IN_BTN_COM)
        element.click()

    def verify_visible_errors(self):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(HomePage.ERROR_MESSAGES_SPAN))
        print("Element is visible? " + str(element.is_displayed()))

    def verify_erors(self, expectedError):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(HomePage.ERROR_MESSAGES_SPAN))
        element = self.driver.find_element(*HomePage.ERROR_MESSAGES_SPAN).text
        erroorMessage = element
        howManyErrors = len(expectedError) - 1
        for iteration, error in enumerate(expectedError):
            if iteration < howManyErrors:
                if error == element:
                    assert erroorMessage == error
            elif iteration == howManyErrors:
                assert erroorMessage == error

    def sing_up_page_btn(self):
        wait = WebDriverWait(self.driver, 60)
        # wait.until(EC.visibility_of_element_located(HomePage.LOGIN_BLOCK))
        # self.driver.find_element(*HomePage.LOGIN_BLOCK)
        wait.until(EC.visibility_of_element_located(HomePage.SIGN_UP_BTN_COM))
        element = self.driver.find_element(*HomePage.SIGN_UP_BTN_COM)
        element.click()











