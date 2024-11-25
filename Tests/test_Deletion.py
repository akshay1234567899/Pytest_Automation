import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest

from Pages.AddCustomer import AddCustomer
from Pages.CustomerLogin import CustomerLogin
from Pages.Customers import Customers
from Pages.Delete import DeletionOfCustomer
from Pages.DepositPage import DepositPage
from Pages.ManagerLogin import ManagerLogin
from Pages.OpenAccount import OpenAccount
from Pages.TransactionsPage import Transactions
from Tests.test_Base import BaseTest


class Test_deletionOfCustomer(BaseTest):
    def test_verificationOfDeletionOfCustomer(self):
        managerLog = ManagerLogin(self.driver)
        managerLog.managerLoginOption()
        addCust = AddCustomer(self.driver)
        addCust.addCustomers()
        delCust = DeletionOfCustomer(self.driver)
        delCust.verifyDeleteCustomer()

    # @pytest.mark.order(1)
    def test_verificationOfWhetherCustomerGotDeletedOrNot(self):
        managerLog = ManagerLogin(self.driver)
        managerLog.managerLoginOption()
        addCust = AddCustomer(self.driver)
        addCust.addCustomers()
        delCust = DeletionOfCustomer(self.driver)
        delCust.verifyDeleteCustomer()
        delCust = DeletionOfCustomer(self.driver)
        delCust.verifyingCustomerDeletedOrNot()
