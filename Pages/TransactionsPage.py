import datetime
import time

import allure

from Configuration.Config import TestData
from LocatorsPackage.Locators import Locators
from Pages.BasePage import BasePage
from allure_commons.types import AttachmentType


class Transactions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyCreditTransactions(self):
        # nowDateTime = datetime.datetime.now()
        # currentDate = nowDateTime.strftime("%B %d, %Y %#I:%M")
        # print('\nCurrent date :', currentDate)
        # currentDateObj = datetime.datetime.strptime(currentDate, "%B %d, %Y %H:%M")
        # date_without_month = currentDateObj.strftime("%d, %Y %H:%M").lstrip("0").replace(" 0", " ")
        # print('\nCurrent date :', date_without_month)
        self.do_click(Locators.TRANSACTIONS_BTN)
        self.do_click(Locators.BACK_BTN)
        self.do_click(Locators.TRANSACTIONS_BTN)
        time.sleep(3)
        # getAmount = self.get_element_text(Locators.AMOUNT_DEPOSITED)
        # print('\nAmount Fetched  :', getAmount)
        # print('\nAmount deposited  :', TestData.DEPOSITING_AMOUNT)
        # assert getAmount == TestData.DEPOSITING_AMOUNT
        # print("TestData.DEPOSITING_AMOUNT" + TestData.DEPOSITING_AMOUNT)
        # allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        getTransactionType = self.get_element_text(Locators.TRANSACTIONS_TYPE_CREDIT)
        assert getTransactionType == "Credit"
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
        print('\nTransaction type :', getTransactionType)
        # getCurrentDateTime = self.get_element_text(Locators.TRANSACTIONS_DATE_TIME)
        # print("getCurrentDateTime : " + self.get_element_text(Locators.TRANSACTIONS_DATE_TIME))
        # getTime = getCurrentDateTime.rpartition(':')[0]
        # date_obj = datetime.datetime.strptime(getTime, "%B %d, %Y %H:%M")
        # getTimeFromTransactions = date_obj.strftime("%d, %Y %H:%M").lstrip("0").replace(" 0", " ")
        # print(getTimeFromTransactions + " = " + date_without_month)
        # assert getTimeFromTransactions == date_without_month
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)

    def verifyDebitTransactions(self):
        self.do_click(Locators.TRANSACTIONS_BTN)
        self.do_click(Locators.BACK_BTN)
        self.do_click(Locators.TRANSACTIONS_BTN)
        time.sleep(5)
        getDebText = self.get_element_text(Locators.TRANSACTIONS_TYPE_DEBIT)
        assert getDebText == "Debit"
