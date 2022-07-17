from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.main_page import MainPage



def test_first(browser_driver):
    wait = WebDriverWait(browser_driver, 10, poll_frequency=1)
    wait.until(EC.title_is("Your Store"))
    browser_driver.find_element(*MainPage.LOGO)
    browser_driver.find_element(*MainPage.SWIPER_UP)
    browser_driver.find_element(*MainPage.SWIPER_DOWN)
    browser_driver.find_element(*MainPage.SEARCH_INPUT)
    assert "Your Store" in browser_driver.title