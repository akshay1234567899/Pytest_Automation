from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage
import allure
from allure_commons.types import AttachmentType


class ManagerLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def managerLoginOption(self):
        self.do_click(Locators.BANK_MANAGER_LOGIN)

    def verifyingTitle(self):
        self.do_click(Locators.BANK_MANAGER_LOGIN)
        title = self.get_title()
        print('\nTitle :', title)
        assert title == "XYZ Bank"
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
