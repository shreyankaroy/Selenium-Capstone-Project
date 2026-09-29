from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------- Locators ----------

    cart_link = (
        By.XPATH,
        "//a[contains(@href,'/view_cart')]"
    )

    cart_product_name = (
        By.CSS_SELECTOR,
        ".cart_description h4 a"
    )

    cart_product_quantity = (
        By.CSS_SELECTOR,
        ".cart_quantity button"
    )

    # ---------- Open Cart ----------

    def open_cart(self):

        self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()

    # ---------- Verify Product ----------

    def is_product_in_cart(self, product_name):

        product = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    f"//td[contains(@class,'cart_description')]"
                    f"//*[contains("
                    f"translate(normalize-space(.),"
                    f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                    f"'abcdefghijklmnopqrstuvwxyz'),"
                    f"'{product_name.lower()}')]"
                )
            )
        )

        return product.is_displayed()

    # ---------- Get Quantity ----------

    def get_product_quantity(self):

        quantity = self.wait.until(
            EC.visibility_of_element_located(
                self.cart_product_quantity
            )
        )

        return quantity.text