import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Pages.AddCustomer import AddCustomer
from Pages.Customers import Customers
from Pages.ManagerLogin import ManagerLogin
from Pages.OpenAccount import OpenAccount

from Pages.CustomerLogin import CustomerLogin
from Tests.test_Base import BaseTest


class Test_CustomerLogin(BaseTest):

    def test_VerifyCombineLogin(self):
        managerLog = ManagerLogin(self.driver)
        managerLog.managerLoginOption()
        addCust = AddCustomer(self.driver)
        addCust.addCustomers()
        openAcnt = OpenAccount(self.driver)
        openAcnt.verifyOpenAccount()
        custVerify = Customers(self.driver)
        custVerify.verifyCustomers()
        custLogin = CustomerLogin(self.driver)
        custLogin.customerLoginOption()

    def test_verifyLoginCustomer(self):
        managerLog = ManagerLogin(self.driver)
        managerLog.managerLoginOption()
        addCust = AddCustomer(self.driver)
        addCust.addCustomers()
        openAcnt = OpenAccount(self.driver)
        openAcnt.verifyOpenAccount()
        custVerify = Customers(self.driver)
        custVerify.verifyCustomers()
        custLogin = CustomerLogin(self.driver)
        custLogin.verifyingLoginCustomer()
