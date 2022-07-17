from selenium.webdriver.common.by import By


class UserRegisterPage:
    FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME = (By.NAME, "lastname")
    EMAIL = (By.ID, "input-email")
    TELEPHONE = (By.NAME, 'telephone')
    NEWSLETTER = (By.NAME, 'newsletter')
