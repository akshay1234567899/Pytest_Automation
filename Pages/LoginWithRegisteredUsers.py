import time

import allure
import xlrd
from allure_commons.types import AttachmentType
from selenium.webdriver.support.select import Select

from Configuration.Config import TestData
from EnumsPackage.Enums import RegisteredCustomers
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class LoginWithRegisteredUser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def logIn(self):
        self.do_click(Locators.CUSTOMER_LOGIN)
        Customers = Select(self.driver.find_element("xpath", "//select[@id='userSelect']"))
        Customers.select_by_visible_text('%s' % str(RegisteredCustomers.ALBUS_DUMBLEDORE.value))
        self.do_click(Locators.CUSTOMER_LOGIN_BTN)
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)



















