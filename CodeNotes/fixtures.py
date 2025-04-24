# fixtures.py
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from pages.signup_page import SignupPage

# from pages.quotes_page import QuoteBlocks


class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n[Fixture] Setting up class resources")
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 5)
        cls.driver.get("https://ns-code-snippet-9eae23357ebe.herokuapp.com/")
        cls.signup_page = SignupPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        print("\n[Fixture] Tearing down class resources")
        cls.driver.quit()
