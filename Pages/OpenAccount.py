import time

import allure
from allure_commons.types import AttachmentType

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage
from selenium.webdriver.support.select import Select


class OpenAccount(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verifyOpenAccount(self):
        self.do_click(Locators.BANK_MANAGER_LOGIN)
        self.do_click(Locators.OPEN_ACCOUNT)
        customers = Select(self.driver.find_element("xpath", "//select[@name='userSelect']"))
        customers.select_by_visible_text(TestData.FULL_NAME)
        print(TestData.FULL_NAME)
        currency = Select(self.driver.find_element("xpath", "//select[@id='currency']"))
        currency.select_by_visible_text("Dollar")
        self.do_click(Locators.PROCESS_BTN)
        self.if_alert()
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
