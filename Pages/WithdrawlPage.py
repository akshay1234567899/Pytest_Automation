import time

import allure
import pytest
from allure_commons.types import AttachmentType

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class Withdrawl(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyWithdrawl(self):
        self.do_click(Locators.WITHDRAWL_BTN)
        self.do_clear(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX)
        time.sleep(3)
        self.do_send_keys(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX, TestData.WITHDRAWL_AMOUNT)
        self.do_click(Locators.WITHDRAW_BTN)
        capturingWithdrawnSuccessfullyMsg = self.get_element_text(Locators.WITHDRAWL_SUCCESSFUL_MSG)
        print('\nWithdrawnSuccessfullyMsg :', capturingWithdrawnSuccessfullyMsg)
        assert capturingWithdrawnSuccessfullyMsg == TestData.SUCCESSFULL_WITHDRAWN_AMT_MSG
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
