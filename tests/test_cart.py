from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

from utilities.csv_reader import CSVReader
from utilities.config_reader import ConfigReader
from utilities.logger import get_logger


# Create logger
logger = get_logger(__name__)


def test_product_in_cart(driver):

    logger.info("Starting product cart test")

    # ---------- Configuration ----------

    config = ConfigReader()

    base_url = config.get_base_url()

    logger.info("Configuration loaded")

    # ---------- Read Test Data ----------

    data = CSVReader.read_data(
        "data/test_data.csv"
    )[0]

    email = data["email"]
    password = data["password"]
    product = data["product"]

    logger.info(
        f"Test data loaded for product: {product}"
    )

    # ---------- Open Website ----------

    logger.info("Opening website")

    driver.get(base_url)

    # ---------- Login ----------

    logger.info("Starting login")

    login_page = LoginPage(driver)

    login_page.click_signup_login()

    login_page.enter_email(email)

    login_page.enter_password(password)

    login_page.click_login()

    logger.info("Login completed successfully")

    # ---------- Go To Products ----------

    logger.info("Opening Products page")

    home_page = HomePage(driver)

    home_page.click_products()

    # ---------- Search Product ----------

    logger.info(
        f"Searching for product: {product}"
    )

    products_page = ProductsPage(driver)

    products_page.search_product(product)

    assert products_page.is_search_result_displayed()

    logger.info("Product search successful")

    # ---------- Add Product To Cart ----------

    logger.info(
        f"Adding product to cart: {product}"
    )

    products_page.add_product_to_cart(product)

    logger.info("Product added to cart successfully")

    # ---------- Open Cart ----------

    logger.info("Opening cart")

    cart_page = CartPage(driver)

    cart_page.open_cart()

    # ---------- Verify Product ----------

    logger.info(
        f"Verifying product in cart: {product}"
    )

    assert cart_page.is_product_in_cart(product)

    logger.info(
        "Product successfully verified in cart"
    )