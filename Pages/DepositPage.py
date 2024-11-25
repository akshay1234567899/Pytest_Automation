import time

import allure
from allure_commons.types import AttachmentType

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class DepositPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verifyDeposit(self):
        self.do_click(Locators.DEPOSIT_BTN)
        self.do_send_keys(Locators.ADD_AMOUNT, TestData.DEPOSITING_AMOUNT)
        print(TestData.DEPOSITING_AMOUNT)
        self.do_click(Locators.AFTER_ADDING_AMOUNT_BTN)
        capturingMsg = self.get_element_text(Locators.DEPOSIT_SUCCESSFULL_MSG)
        print(capturingMsg)
        assert capturingMsg == TestData.SUCCESSFULLY_DEPOSIT_AMT_MSG
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
