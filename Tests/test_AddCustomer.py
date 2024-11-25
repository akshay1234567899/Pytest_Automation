import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Pages.AddCustomer import AddCustomer
from Pages.ManagerLogin import ManagerLogin
from Tests.test_Base import BaseTest


class Test_AddCustomer(BaseTest):

    def test_verifyAddCustomer(self):
        managerLog = ManagerLogin(self.driver)
        managerLog.managerLoginOption()
        addCust = AddCustomer(self.driver)
        addCust.addCustomers()
