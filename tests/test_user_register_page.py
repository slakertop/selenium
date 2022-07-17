from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.user_register_page import UserRegisterPage


def test_admin_login_page(browser_driver):
    browser_driver.get(browser_driver.url + 'index.php?route=account/register')
    wait = WebDriverWait(browser_driver, 10, poll_frequency=1)
    wait.until(EC.title_is("Register Account"))
    wait.until(EC.visibility_of_element_located(UserRegisterPage.EMAIL))
    browser_driver.find_element(*UserRegisterPage.FIRSTNAME)
    browser_driver.find_element(*UserRegisterPage.LASTNAME)
    browser_driver.find_element(*UserRegisterPage.EMAIL)
    browser_driver.find_element(*UserRegisterPage.TELEPHONE)
    browser_driver.find_element(*UserRegisterPage.NEWSLETTER)
    assert "Register Account" in browser_driver.title
