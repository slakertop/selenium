from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.admin_login_page import AdminLoginPage


def test_admin_login_page(browser_driver):
    browser_driver.get(browser_driver.url + 'admin')
    wait = WebDriverWait(browser_driver, 10, poll_frequency=1)
    wait.until(EC.title_is("Administration"))
    wait.until(EC.visibility_of_element_located(AdminLoginPage.SUBMIT))
    browser_driver.find_element(*AdminLoginPage.USERNAME)
    browser_driver.find_element(*AdminLoginPage.PASSWORD)
    browser_driver.find_element(*AdminLoginPage.SUBMIT)
    browser_driver.find_element(*AdminLoginPage.FORGOTTENPASSWORD)
    browser_driver.find_element(*AdminLoginPage.PANELTITLE)
    assert "Administration" in browser_driver.title
