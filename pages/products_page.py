from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ---------- Locators ----------

    search_box = (
        By.ID,
        "search_product"
    )

    search_button = (
        By.ID,
        "submit_search"
    )

    searched_products_heading = (
        By.XPATH,
        "//h2[contains(text(),'Searched Products')]"
    )

    # ---------- Search Product ----------

    def search_product(self, product_name):

        search = self.wait.until(
            EC.visibility_of_element_located(
                self.search_box
            )
        )

        search.clear()

        search.send_keys(product_name)

        self.wait.until(
            EC.element_to_be_clickable(
                self.search_button
            )
        ).click()

    # ---------- Verify Search Result ----------

    def is_search_result_displayed(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.searched_products_heading
            )
        ).is_displayed()

    # ---------- Add Product To Cart ----------

    def add_product_to_cart(self, product_name):

        product = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    f"//div[contains(@class,'productinfo')]"
                    f"//p[contains("
                    f"translate(normalize-space(.),"
                    f"'ABCDEFGHIJKLMNOPQRSTUVWXYZ',"
                    f"'abcdefghijklmnopqrstuvwxyz'),"
                    f"'{product_name.lower()}')]"
                )
            )
        )

        product_card = product.find_element(
            By.XPATH,
            "./ancestor::div[contains(@class,'product-image-wrapper')]"
        )

        add_to_cart = product_card.find_element(
            By.CSS_SELECTOR,
            "a.add-to-cart"
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            add_to_cart
        )

        self.wait.until(
            EC.element_to_be_clickable(
                add_to_cart
            )
        ).click()