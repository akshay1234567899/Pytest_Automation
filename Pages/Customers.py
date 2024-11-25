import time

import allure
from allure_commons.types import AttachmentType

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class Customers(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyCustomers(self):
        self.do_click(Locators.CUSTOMERS)
        cust = self.driver.find_element("xpath", "//td[contains(text(),'%s')]" % int(TestData.POST_CODE))
        print('\nCustomer Post Code :', cust.text)
        assert cust.text == TestData.POST_CODE
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)


