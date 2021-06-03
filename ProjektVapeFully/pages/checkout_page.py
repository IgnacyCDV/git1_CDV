from selenium.webdriver.common.keys import Keys
from time import sleep
from pages.base_page import BasePage
from locatorsy import CheckOutPages
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckOutPage(BasePage):
    def form_check_email(self, email,deley):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(CheckOutPages.EMAIL_FIELD))
        fill_email = self.driver.find_element(*CheckOutPages.EMAIL_FIELD)
        for c in email:
            fill_email.send_keys(c)
            sleep(deley)

    def form_check_name(self, name):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(CheckOutPages.NAME_FIELD))
        fill_name = self.driver.find_element(*CheckOutPages.NAME_FIELD)
        fill_name.send_keys(name)
    def form_check_lastname(self, lastname):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(CheckOutPages.LASTNAME_FIELD))
        fill_lastname = self.driver.find_element(*CheckOutPages.LASTNAME_FIELD)
        fill_lastname.send_keys(lastname)
    def form_check_country(self, country):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(CheckOutPages.COUNTRY_FIELD))
        fill_country = self.driver.find_element(*CheckOutPages.COUNTRY_FIELD)
        fill_country.click()
        search = wait.until(EC.element_to_be_clickable(CheckOutPages.COUNTRY_SEARCH))
        search.click()
        search.send_keys(country)
        search.send_keys(Keys.ENTER)

    def form_check_address(self, address):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(CheckOutPages.ADDRESS_FIELD))
        fill_address= self.driver.find_element(*CheckOutPages.ADDRESS_FIELD)
        fill_address.send_keys(address)
    def form_check_postcode(self, postcode):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(CheckOutPages.POSTCODE_FIELD))
        fill_postcode = self.driver.find_element(*CheckOutPages.POSTCODE_FIELD)
        fill_postcode.send_keys(postcode)
    def form_check_city(self, city):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(CheckOutPages.CITY_FIELD))
        fill_city = self.driver.find_element(*CheckOutPages.CITY_FIELD)
        fill_city.send_keys(city)
    def form_check_phone(self, phone):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(CheckOutPages.PHONE_FIELD))
        fill_phone = self.driver.find_element(*CheckOutPages.PHONE_FIELD)
        fill_phone.send_keys(phone)
    def form_check_ihaveread(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(CheckOutPages.IHAVER_BOX))
        fill_box = self.driver.find_element(*CheckOutPages.IHAVER_BOX)
        fill_box.click()
    def from_check_placeorder(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located(CheckOutPages.PLACE_ORDER_BTN))
        place_order = self.driver.find_element(*CheckOutPages.PLACE_ORDER_BTN)
        place_order.click()
    def check_URL(self):
        URL = self.driver.current_url
        expected_URL = "https://secure.payu.com/pay/"
        if expected_URL in URL:
            assert 1==1
        else:
            assert 1==0
    def click_outside(self):
        element = self.driver.find_element(*CheckOutPages.OUTSIDE)
        element.click()
        print("kilk")