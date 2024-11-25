import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver.maximize_window()
        web_driver.implicitly_wait(10)
        web_driver.delete_all_cookies()
    else:
        "firefox" == request.param
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        web_driver.maximize_window()
        web_driver.delete_all_cookies()
    request.cls.driver = web_driver
    yield
    web_driver.close()

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
