from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locators


class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_signup_btn(self):
        element = self.wait.until(EC.presence_of_element_located(Locators.SIGNUP))
        self.driver.execute_script("arguments[0].click();", element)

    def enter_email(self, email):
        element = self.wait.until(EC.presence_of_element_located(Locators.EMAIL_INPUT))
        self.driver.execute_script("arguments[0].value = arguments[1];", element, email)

    def enter_password(self, password):
        element = self.wait.until(
            EC.presence_of_element_located(Locators.PASSWORD_INPUT)
        )
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", element, password
        )

    def enter_confirm_password(self, confirmpassword):
        element = self.wait.until(
            EC.presence_of_element_located(Locators.CONFIRM_PASSWORD_INPUT)
        )
        self.driver.execute_script(
            "arguments[0].value = arguments[1];", element, confirmpassword
        )

    def click_signup_submit_button(self):
        button = self.wait.until(EC.presence_of_element_located(Locators.SIGNUP_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)

    # Optional methods you can enable if needed
    # def is_logout_link_visible(self):
    #     element = self.wait.until(EC.presence_of_element_located(Locators.LOGOUT_BUTTON))
    #     return element.text

    # def login_error_msg(self):
    #     return self.wait.until(EC.presence_of_element_located(Locators.LOGIN_ERROR)).text
