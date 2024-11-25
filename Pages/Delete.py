import time

import allure
from allure_commons.types import AttachmentType
from collections.abc import Mapping
from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class DeletionOfCustomer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyDeleteCustomer(self):
        self.do_click(Locators.BANK_MANAGER_LOGIN)
        self.do_click(Locators.CUSTOMERS)
        self.do_send_keys(Locators.SEARCH_CUSTOMERS, TestData.FIRST_NAME)
        self.do_click(Locators.DELETE_CUSTOMERS)
        self.do_click(Locators.HOME_BTN)
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def verifyingCustomerDeletedOrNot(self):
        self.do_click(Locators.BANK_MANAGER_LOGIN)
        self.do_click(Locators.CUSTOMERS)
        try:
            self.do_send_keys(Locators.SEARCH_CUSTOMERS, TestData.FIRST_NAME)
            self.do_click(Locators.DELETE_CUSTOMERS)
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        except:
            pass
            print("No customer with name, " + TestData.FIRST_NAME + " is registered with our bank..")
