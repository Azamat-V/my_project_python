"""
Conftest is a configuration file for tests it applies to all tests you want to apply
All fixtures are usually stored in this file
"""

import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage


@pytest.fixture()
# Fixture without attributes applies to method
def set_up():
    print("Preconditions of the  method(test)")
    yield
    print("Post conditions of the method(test)")


@pytest.fixture(scope="class")
# Fixture with attributes applies to the attributes like scope="class" or "module"
def one_time_set_up(request, browser):
    print("Preconditions(Class or Module)")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_web_driver_instance()
    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")


    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Post conditions(Class or module)")



def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

# This methods get options to execute code with different provided browsers and osType etg. --browser, --osType
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")



