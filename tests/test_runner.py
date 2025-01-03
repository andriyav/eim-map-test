import os
import unittest
from selenium import webdriver
from SLP.ui.PageObjects.SLPlogin.slp_login import LoginComponent
from SLP.ui.PageObjects.login_modal.login_modal import LoginModal
from data.value_provider import ValueProvider

CHROME_USER_DIR_LOCAL = '/home/runner/.config/google-chrome/'
CHROME_USER_DIR_GIT = './tests/cache'

IMPLICITLY_WAIT = 10


class BaseTestRunner(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self._init_driver()
        self._login()

    '''Login with username and password'''

    def _init_driver(self):
        if os.getenv('CI') == 'true' and os.getenv('GITHUB_ACTIONS') == 'true':
            chrome_user_dir = CHROME_USER_DIR_GIT

        else:
            chrome_user_dir = CHROME_USER_DIR_LOCAL
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"user-data-dir={chrome_user_dir}")
        chrome_options.add_argument("profile-directory=Default")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.driver.maximize_window()
        self.driver.get(ValueProvider.get_base_url())

    def _login(self):
        self.driver.implicitly_wait(10)
        LoginComponent(self.driver).click_authorisation_btn()
        # LoginModal(self.driver).set_email(ValueProvider.get_email())
        # LoginModal(self.driver).click_next_button_first()
        # LoginModal(self.driver).set_password(ValueProvider.get_password())
        # LoginModal(self.driver).click_next_button_second()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
