from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # ---------- Locators ----------

    products_link = (
        By.XPATH,
        "//a[@href='/products']"
    )

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

    # ---------- Open Products ----------

    def click_products(self):

        products = self.wait.until(
            EC.element_to_be_clickable(
                self.products_link
            )
        )

        products.click()

        # Wait until Products page is loaded
        self.wait.until(
            EC.visibility_of_element_located(
                self.search_box
            )
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