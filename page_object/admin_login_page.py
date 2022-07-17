from selenium.webdriver.common.by import By


class AdminLoginPage:
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.CLASS_NAME, "btn-primary")
    PANELTITLE = (By.CLASS_NAME, "panel-title")
    FORGOTTENPASSWORD = (By.CSS_SELECTOR, "a[href]")
