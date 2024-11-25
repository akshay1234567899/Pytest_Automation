import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''This class is the parent of all pages'''
'''It contains all generic methods and utilities for all the pages'''


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_clear(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).clear()

    def do_click(self, by_locator):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        time.sleep(2)
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self):
        time.sleep(2)
        return self.driver.title

    def if_alert(self):
        time.sleep(2)
        alertHandle = self.driver.switch_to.alert
        alertHandle.accept()
