import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    """
    Klasa bazowa każdego testu
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://dev.eu.mywoocart.com/")
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()