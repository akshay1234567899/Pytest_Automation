import random
import string
from faker import Faker


class TestData:
    fake = Faker()
    BASE_URL = "https://globalsqa.com/angularJs-protractor/BankingProject/#/login"
    REGISTERED_USER = "Albus Dumbledore"
    DEPOSITING_AMOUNT = random.randint(10000, 50000)
    SUCCESSFULLY_DEPOSIT_AMT_MSG = "Deposit Successful"
    WITHDRAWL_AMOUNT = random.randint(1000, 5000)
    SUCCESSFULL_WITHDRAWN_AMT_MSG = "Transaction successful"
    FAILED_WITHDRAWN_MSG = "Transaction Failed. You can not withdraw amount more than the balance."
    FIRST_NAME = fake.first_name()
    LAST_NAME = fake.last_name()
    POST_CODE = fake.postcode()
    FULL_NAME = FIRST_NAME + " " + LAST_NAME
