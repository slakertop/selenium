from selenium.webdriver.common.by import By


class CatalogPage:
    PRODUCT = (By.CSS_SELECTOR, ".product-thumb")
    LIST = (By.CLASS_NAME, "list-group")
    ARTICLE = (By.CSS_SELECTOR, "div#content>h2")
    HEADER = (By.CSS_SELECTOR, "#top")
    PAGE = (By.ID, 'product-category')
