from selenium.webdriver.common.by import By


class Locators:
    CUSTOMER_LOGIN = (By.XPATH, "//button[text()='Customer Login']")
    YOUR_NAME = (By.XPATH, "//select[@id='userSelect']")
    CUSTOMER_LOGIN_BTN = (By.XPATH, "//button[text()='Login']")
    '''Deposit'''
    DEPOSIT_BTN = (By.XPATH, "//button[contains(text(),'Deposit')]")
    ADD_AMOUNT = (By.XPATH, "//input[@placeholder='amount']")
    AFTER_ADDING_AMOUNT_BTN = (By.XPATH, "(//button[contains(text(),'Deposit')])[2]")
    DEPOSIT_SUCCESSFULL_MSG = (By.XPATH, "//span[text()='Deposit Successful']")
    '''Transactions'''
    TRANSACTIONS_BTN = (By.XPATH, "//button[contains(text(),'Trans')]")
    TRANSACTIONS_TYPE_CREDIT = (By.XPATH, "(//td[contains(text(),'Credit')])[1]")
    TRANSACTIONS_DATE_TIME = (By.XPATH, "//tr[@id='anchor0']//td[contains(text(),'M')]")
    TRANSACTIONS_TYPE_DEBIT = (By.XPATH, "//td[contains(text(),'Debit')]")
    AMOUNT_DEPOSITED = (By.XPATH, "(//tr[@id='anchor0']//td[@class='ng-binding'])[2]")
    AMOUNT_WITHDRAWN = (By.XPATH, "(//tr[@id='anchor0']//td[@class='ng-binding'])[2]")
    '''Withdrawl'''
    WITHDRAWL_BTN = (By.XPATH, "//button[contains(text(),'Withdrawl')]")
    AMOUNT_TO_BE_WITHDRAWN_TEXTBOX = (By.XPATH, "//div[@class='form-group']//input[@type='number']")
    WITHDRAW_BTN = (By.XPATH, "//button[text()='Withdraw']")
    WITHDRAWL_SUCCESSFUL_MSG = (By.XPATH, "//span[text()='Transaction successful']")
    WITHDRAWL_UNSUCCESSFUL_MSG = (By.XPATH, "//span[contains(text(),'Transaction Failed.')]")
    '''Manager Options'''
    BANK_MANAGER_LOGIN = (By.XPATH, "//button[text()='Bank Manager Login']")
    TITLE = (By.XPATH, "//title[text()='XYZ Bank']")
    OPEN_ACCOUNT = (By.XPATH, "//button[contains(text(),'Open Account')]")
    CUSTOMERS = (By.XPATH, "//button[@ng-click='showCust()']")
    '''Add Customers'''
    ADD_CUSTOMERS = (By.XPATH, "//button[contains(text(),'Add Customer')]")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    POST_CODE = (By.XPATH, "//input[@placeholder='Post Code']")
    ADD_CUSTOMER_BTN = (By.XPATH, "//button[text()='Add Customer']")

    HOME_BTN = (By.XPATH, "//button[text()='Home']")
    BACK_BTN = (By.XPATH, "//button[text()='Back']")
    PROCESS_BTN = (By.XPATH, "//button[@type='submit']")
    VERIFYING_CUSTOMER_USING_POSTCODE = (By.XPATH, "//td[contains(text(),{Testdata.POST_CODE})]")
    SEARCH_CUSTOMERS = (By.XPATH, "//input[@placeholder='Search Customer']")
    DELETE_CUSTOMERS = (By.XPATH, "//button[text()='Delete']")