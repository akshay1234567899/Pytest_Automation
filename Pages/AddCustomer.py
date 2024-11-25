import allure
from allure_commons.types import AttachmentType

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class AddCustomer(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def addCustomers(self):
        self.do_click(Locators.ADD_CUSTOMERS)
        self.do_send_keys(Locators.FIRST_NAME, TestData.FIRST_NAME)
        print('\nFirst Name :', TestData.FIRST_NAME)
        self.do_send_keys(Locators.LAST_NAME, TestData.LAST_NAME)
        print('\nLast Name :', TestData.LAST_NAME)
        self.do_send_keys(Locators.POST_CODE, TestData.POST_CODE)
        print(TestData.FULL_NAME)
        print('\nPost Code :', TestData.POST_CODE)
        self.do_click(Locators.ADD_CUSTOMER_BTN)
        self.if_alert()
        self.do_click(Locators.HOME_BTN)
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
