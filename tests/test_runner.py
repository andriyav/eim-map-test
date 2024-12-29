import os
import time
import unittest
from selenium import webdriver
from SLP.ui.PageObjects.SLPlogin.slp_login import LoginComponent
from SLP.ui.PageObjects.login_modal.login_modal import LoginModal
from data.value_provider import ValueProvider

# CHROME_USER_DIR = 'C:/Users/aandrusy/ssh_repos/private/SLPUI/tests/cache'
CHROME_USER_DIR = './tests/cache'

IMPLICITLY_WAIT = 10


class BaseTestRunner(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self._init_driver()
        self._login()

    '''Login with username and password'''

    def _init_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"user-data-dir={CHROME_USER_DIR}")
        chrome_options.add_argument("profile-directory=Default")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.driver.maximize_window()
        self.driver.get(ValueProvider.get_base_url())

    def _login(self):
        self.driver.implicitly_wait(10)
        LoginComponent(self.driver).click_authorisation_btn()


    def tearDown(self):
        self.driver.quit()