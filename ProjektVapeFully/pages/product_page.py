from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locatorsy import ProductPages
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class ProductPage(BasePage):
    """
        Strona produktu
        """

    def product_search(self, product):
        wait = WebDriverWait(self.driver, 60)
        element = wait.until(EC.visibility_of_element_located(ProductPages.SEARSH_FIELD))
        element.send_keys(product)
        element2 = wait.until(EC.visibility_of_element_located(ProductPages.AUTOSUGGESTION_FIELD))
        element2.click()

    def variable_product_choose(self, choosen_variant):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located(ProductPages.VARIANTS_OPEN))
        element.click()
        variants = self.driver.find_elements_by_xpath(ProductPages.VARIANTS_SELLECT)
        for variant in variants:
            if variant.text == choosen_variant:
                variant.click()

    def add_to_basket(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(ProductPages.ADD_TO_CARTV))
        element = self.driver.find_element(*ProductPages.ADD_TO_CART)
        ## Przewiń stronę, element w centrum
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        desired_y = (element.size['height'] / 2) + element.location['y']
        current_y = (self.driver.execute_script('return window.innerHeight') / 2) + self.driver.execute_script(
            'return window.pageYOffset')
        scroll_y_by = desired_y - current_y
        self.driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
        sleep(2)
        element.click()
    def go_to_cart(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(ProductPages.CART_BTN))
        element = self.driver.find_element(*ProductPages.CART_BTN)
        element.click()

        # for i in variants:
        #     print(i)




