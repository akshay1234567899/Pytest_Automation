import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.select import Select

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage


class CustomerLogin(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def customerLoginOption(self):
        self.do_click(Locators.CUSTOMER_LOGIN)
        Customers = Select(self.driver.find_element("xpath", "//select[@id='userSelect']"))
        Customers.select_by_visible_text(TestData.FULL_NAME)
        self.do_click(Locators.CUSTOMER_LOGIN_BTN)
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def verifyingLoginCustomer(self):
        self.do_click(Locators.CUSTOMER_LOGIN)
        Customers = Select(self.driver.find_element("xpath", "//select[@id='userSelect']"))
        Customers.select_by_visible_text(TestData.FULL_NAME)
        self.do_click(Locators.CUSTOMER_LOGIN_BTN)
        elementRec = self.driver.find_element("xpath", "//strong[text()=' Welcome ']//span[text()='%s']" %
                                              str(TestData.FULL_NAME))
        print('\nCustomer name:', elementRec.text)
        assert elementRec.text == TestData.FULL_NAME
        print('\nTest data full name :', TestData.FULL_NAME)
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
