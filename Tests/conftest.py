from idlelib import browser

from selenium import webdriver

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.microsoft import EdgeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest


@pytest.fixture(params=["chrome", "edge", "firefox"], scope='class')
def init_driver(request):
    # Get the browser name from request.param
    browser = request.param

    if browser == 'edge':
        # Initialize Edge WebDriver (currently commented out in your code)
        # driver = webdriver.Edge(EdgeDriverManager().install())
        print("Launching Edge browser.........")

    elif browser == 'firefox':
        # Initialize Firefox WebDriver using Service for newer Selenium versions
        firefox_service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service)
        print("Launching Firefox browser.........")

    else:
        # Initialize Chrome WebDriver using Service for newer Selenium versions
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service)
        print("Launching Chrome browser.........")

    # Common setup for all browsers
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()

    # Assign the driver to the test class for access
    request.cls.driver = driver
    yield driver  # Yield the driver to the test

    # After the test, quit the driver to close the browser
    driver.quit()

#
# def __init__(self):
#     self.unittest_location = os.sep.join(pytest.__file__.split(os.sep)[:-1])
#     self.stderr = sys.__stderr__
#     self.skip = False
#
#
# def write(self, text):
#     if self.skip and text.find("\n") != -1:
#         self.skip = False
#     elif self.skip:
#         pass
#     else:
#         self.skip = text.find(self.unittest_location) != -1
#         if not self.skip: self.stderr.write(text)
#
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Sauce Demo'
#     config._metadata['Tester'] = 'Saurav'
