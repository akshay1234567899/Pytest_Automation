import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Pages.LoginWithRegisteredUsers import LoginWithRegisteredUser
from Tests.test_Base import BaseTest


class Test_LoginWithRegisteredUser(BaseTest):

    def test_verifyLoginWithRegisteredUsers(self):
        registerCust = LoginWithRegisteredUser(self.driver)
        registerCust.logIn()
