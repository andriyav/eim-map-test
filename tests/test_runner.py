import time
import unittest
from selenium import webdriver

from SLP.ui.PageObjects.login_modal.login_components import LoginComponent
from SLP.ui.PageObjects.login_modal.login_modal import LoginModal
from tests.value_provider import ValueProvider

IMPLICITLY_WAIT = 10


class BaseTestRunner(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self._init_driver()
        self._login()

    def _init_driver(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.driver.maximize_window()
        self.driver.get(ValueProvider.get_base_url())

    def _login(self):
        self.driver.implicitly_wait(30)
        LoginComponent(self.driver).click_authorisation_btn()
        LoginModal(self.driver).set_email(ValueProvider.get_email())
        LoginModal(self.driver).click_next_button_first()
        time.sleep(10)
        LoginModal(self.driver).set_password(ValueProvider.get_password())
        time.sleep(10)
        LoginModal(self.driver).click_next_button_second()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()
