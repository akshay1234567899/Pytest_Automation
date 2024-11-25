import time

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class WithdrawlAmountWithRegisteredUser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyAmountWithdrawlWithRedUsers(self):
        self.do_click(Locators.WITHDRAWL_BTN)
        self.do_send_keys(Locators.AMOUNT_TO_BE_WITHDRAWN_TEXTBOX, TestData.WITHDRAWL_AMOUNT)
        self.do_click(Locators.WITHDRAW_BTN)
        try:
            capturingWithdrawnSuccessfullyMsg = self.get_element_text(Locators.WITHDRAWL_SUCCESSFUL_MSG)
            print('\nCaptured Msg :', capturingWithdrawnSuccessfullyMsg)
            assert capturingWithdrawnSuccessfullyMsg == TestData.SUCCESSFULL_WITHDRAWN_AMT_MSG
            allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        except TimeoutException:
            raise TimeoutError("Your request has been timed out! Try overriding timeout!")
        except NoSuchElementException:
            return "None"
        except Exception:
            return "None"
