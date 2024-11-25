import os
import sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Pages.DepositingAmountWithRegisteredUser import DepositingAmountWithRegisteredUser
from Pages.LoginWithRegisteredUsers import LoginWithRegisteredUser
from Pages.WithdrawlAmountWithRegisteredUser import WithdrawlAmountWithRegisteredUser
from Tests.test_Base import BaseTest


class Test_WithdrawlAmountWithRegisteredUser(BaseTest):
    def test_WithdrawingAmountWithRegUsers(self):
        registerCust = LoginWithRegisteredUser(self.driver)
        registerCust.logIn()
        depoAmount = DepositingAmountWithRegisteredUser(self.driver)
        depoAmount.verifyDepoAmountWithRegisteredUser()
        withdrewAmount = WithdrawlAmountWithRegisteredUser(self.driver)
        withdrewAmount.verifyAmountWithdrawlWithRedUsers()
