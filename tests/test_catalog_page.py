from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.catalog_page import CatalogPage


def test_catalog_page(browser_driver):
    browser_driver.get(browser_driver.url + 'laptop-notebook')
    wait = WebDriverWait(browser_driver, 10, poll_frequency=1)
    wait.until(EC.title_is("Laptops & Notebooks"))
    wait.until(EC.visibility_of_element_located(CatalogPage.PRODUCT))
    browser_driver.find_element(*CatalogPage.PRODUCT)
    browser_driver.find_element(*CatalogPage.LIST)
    browser_driver.find_elements(*CatalogPage.PRODUCT)
    browser_driver.find_element(*CatalogPage.HEADER)
    browser_driver.find_element(*CatalogPage.ARTICLE)
    browser_driver.find_element(*CatalogPage.PAGE)
    print(len(browser_driver.find_elements(*CatalogPage.PRODUCT)))
    assert len(browser_driver.find_elements(*CatalogPage.PRODUCT)) > 0
    assert "Laptops & Notebooks" in browser_driver.title
