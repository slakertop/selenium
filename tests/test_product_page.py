from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.product_page import ProductPage


def test_admin_login_page(browser_driver):
    browser_driver.get(browser_driver.url + 'desktops/test')
    wait = WebDriverWait(browser_driver, 10, poll_frequency=1)
    wait.until(EC.title_is("Apple Cinema 30"))
    wait.until(EC.visibility_of_element_located(ProductPage.PRODUCT_DESCRIPTION))
    browser_driver.find_element(*ProductPage.IMAGE)
    browser_driver.find_element(*ProductPage.PRODUCT_DESCRIPTION)
    browser_driver.find_element(*ProductPage.BUTTON)
    browser_driver.find_element(*ProductPage.ALERT)
    browser_driver.find_element(*ProductPage.INPUT_OPTION)
    assert "Apple Cinema 30" in browser_driver.title
