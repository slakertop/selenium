from selenium.webdriver.common.by import By


class ProductPage:
    IMAGE = (By.CSS_SELECTOR, ".thumbnail")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#product")
    INPUT_OPTION = (By.ID, 'input-option208')
    BUTTON = (By.ID, 'button-cart')
    ALERT = (By.CLASS_NAME, 'alert-info')
