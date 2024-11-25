import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Pages.AddCustomer import AddCustomer
from Pages.CustomerLogin import CustomerLogin
from Pages.Customers import Customers
from Pages.DepositPage import DepositPage
from Pages.ManagerLogin import ManagerLogin
from Pages.OpenAccount import OpenAccount
from Tests.test_Base import BaseTest


class Test_Deposit(BaseTest):
    def test_verifyDeposit(self):
        managerLog = ManagerLogin(self.driver)
        managerLog.managerLoginOption()
        addCust = AddCustomer(self.driver)
        addCust.addCustomers()
        openAcnt = OpenAccount(self.driver)
        openAcnt.verifyOpenAccount()
        custVerify = Customers(self.driver)
        custVerify.verifyCustomers()
        combineLogin = CustomerLogin(self.driver)
        combineLogin.customerLoginOption()
        depositAmnt = DepositPage(self.driver)
        depositAmnt.verifyDeposit()
