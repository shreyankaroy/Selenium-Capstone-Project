import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from utilities.csv_reader import CSVReader
from utilities.config_reader import ConfigReader
from utilities.logger import get_logger


logger = get_logger(__name__)


class LoginTest(unittest.TestCase):

    def setUp(self):

        logger.info("Starting Unittest login test")

        # Read configuration
        config = ConfigReader()

        self.base_url = config.get_base_url()

        # Start browser
        self.driver = webdriver.Chrome()

        self.driver.maximize_window()

        logger.info("Browser started")

    def test_login(self):

        logger.info("Opening website")

        self.driver.get(self.base_url)

        # Read CSV data
        data = CSVReader.read_data(
            "data/test_data.csv"
        )[0]

        email = data["email"]
        password = data["password"]

        # Login
        login_page = LoginPage(self.driver)

        login_page.click_signup_login()

        login_page.enter_email(email)

        login_page.enter_password(password)

        login_page.click_login()

        logger.info("Login completed")

        # Verify login
        assert "Logged in as" in self.driver.page_source

        logger.info("Login verification successful")

    def tearDown(self):

        logger.info("Closing browser")

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()