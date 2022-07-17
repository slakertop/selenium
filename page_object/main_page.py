from selenium.webdriver.common.by import By


class MainPage:
    LOGO = (By.CSS_SELECTOR, "#logo")
    SEARCH_INPUT = (By.NAME, "search")
    SWIPER_UP = (By.CLASS_NAME, "swiper-wrapper")
    SWIPER_DOWN = (By.ID, "carousel0")
    CART_TOTAL = (By.ID, "cart-total")
