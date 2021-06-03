from locatorsy import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LoginPageCom(BasePage):
    """
    Strona rejestracji
    """
    def _verify_page(self):
        print("Weryfikacja RegistartionPage")
        # Tutaj będziemy weryfikować stronę
        wait = WebDriverWait(self.driver, 60)
        # Wywołanie metody until na obiekcie WebDriverWait
        # W efekcie otrzymamy element (jeśli warunek wystąpi)
        wait.until(EC.presence_of_element_located((HomePage.MY_ACCOUNT_BTN_COM)))



