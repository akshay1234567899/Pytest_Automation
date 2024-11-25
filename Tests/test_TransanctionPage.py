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
from Pages.TransactionsPage import Transactions
from Pages.WithdrawlPage import Withdrawl
from Tests.test_Base import BaseTest


class Test_Transactions(BaseTest):
    def test_verifyingCreditTransactions(self):
        managerLog = ManagerLogin(self.driver)
        managerLog.managerLoginOption()
        addCust = AddCustomer(self.driver)
        addCust.addCustomers()
        openAcnt = OpenAccount(self.driver)
        openAcnt.verifyOpenAccount()
        custVerify = Customers(self.driver)
        custVerify.verifyCustomers()
        customerLogin = CustomerLogin(self.driver)
        customerLogin.customerLoginOption()
        depositAmnt = DepositPage(self.driver)
        depositAmnt.verifyDeposit()
        transaction = Transactions(self.driver)
        transaction.verifyCreditTransactions()

    def test_verifyingDebitTransactions(self):
        managerLog = ManagerLogin(self.driver)
        managerLog.managerLoginOption()
        addCust = AddCustomer(self.driver)
        addCust.addCustomers()
        openAcnt = OpenAccount(self.driver)
        openAcnt.verifyOpenAccount()
        custVerify = Customers(self.driver)
        custVerify.verifyCustomers()
        customerLogin = CustomerLogin(self.driver)
        customerLogin.customerLoginOption()
        depositAmnt = DepositPage(self.driver)
        depositAmnt.verifyDeposit()
        withdrawnAmnt = Withdrawl(self.driver)
        withdrawnAmnt.verifyWithdrawl()
        transaction = Transactions(self.driver)
        transaction.verifyDebitTransactions()

