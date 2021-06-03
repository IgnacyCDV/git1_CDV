from pages.base_page import BasePage
from locatorsy import CartPages
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    def item_check(self, product):
        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.visibility_of_element_located(CartPages.PRODUCT_NAME))
        text_element = element.text
        if product in text_element:
            assert 1==1
        else:
            assert 1==0

    def free_courier(self, product):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located(CartPages.PRODUCT_PRICE))
        text_element = element.text
        element2 = wait.until(EC.visibility_of_element_located(CartPages.SHIPPING_METHOD))
        text_element2 = element2.text
        element3  = self.driver.find_element(*CartPages.TOTAL_PRICE)
        text_element3 = element3.text
        if "FREE" in text_element2:
            assert text_element == text_element3
        else:
            assert 1==0
    def go_to_chekout(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located(CartPages.CHECKOUT_BTN))
        element.click()






