import pytest
from selenium import webdriver
import os


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--url", action="store", default="http://192.168.0.109:8081/")


@pytest.fixture
def browser_driver(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    url = request.config.getoption("--url")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=drivers + '/chromedriver')
    elif browser == 'firefox':
        driver = webdriver.Chrome(executable_path=drivers + '/geckodriver')
    elif browser == 'opera':
        driver = webdriver.Chrome(executable_path=drivers + '/operadriver')
    else:
        driver = webdriver.Safari()

    driver.get(url)
    driver.url = url
    request.addfinalizer(driver.close)
    return driver
