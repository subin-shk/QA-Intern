from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase
import unittest
from selenium.common.exceptions import TimeoutException

from locator import Locators
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fixtures import BaseTest


class CodeNotes(BaseTest):
    def test_valid_login(self):
        self.signup_page.click_signup_btn()
        self.signup_page.enter_email("username@gmail.com")
        self.signup_page.enter_password("password123")
        self.signup_page.enter_confirm_password("password123")
        self.signup_page.click_signup_submit_button()

        # expected_result = "https://quotes.toscrape.com/login"
        # # self.driver.implicitly_wait(1)
        # try:
        #     actual_result = self.driver.current_url
        #     self.assertNotEqual(
        #         actual_result, expected_result, "Failed: User was not able to login"
        #     )

        #     print("Pass: User was able to login")
        # except AssertionError as e:
        #     print(e)
