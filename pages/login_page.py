from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ---------- Locators ----------

    signup_login_link = (
        By.XPATH,
        "//a[contains(text(),'Signup / Login')]"
    )

    email_field = (
        By.CSS_SELECTOR,
        "input[data-qa='login-email']"
    )

    password_field = (
        By.CSS_SELECTOR,
        "input[data-qa='login-password']"
    )

    login_button = (
        By.CSS_SELECTOR,
        "button[data-qa='login-button']"
    )

    # ---------- Actions ----------

    def click_signup_login(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.signup_login_link
            )
        ).click()

        # Wait until the login email field appears
        self.wait.until(
            EC.visibility_of_element_located(
                self.email_field
            )
        )

    def enter_email(self, email):

        self.wait.until(
            EC.visibility_of_element_located(
                self.email_field
            )
        ).clear()

        self.driver.find_element(
            *self.email_field
        ).send_keys(email)

    def enter_password(self, password):

        self.wait.until(
            EC.visibility_of_element_located(
                self.password_field
            )
        ).clear()

        self.driver.find_element(
            *self.password_field
        ).send_keys(password)

    def click_login(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.login_button
            )
        ).click()