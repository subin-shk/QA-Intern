from selenium.webdriver.common.by import By


class Locators:
    SIGNUP = (By.XPATH, '//a[text()="Sign Up"]')
    EMAIL_INPUT = (By.ID, "user_email")
    PASSWORD_INPUT = (By.ID, "user_password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "user_password_confirmation")
    SIGNUP_BUTTON = (By.NAME, "commit")
