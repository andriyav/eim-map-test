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
        # LoginModal(self.driver).set_email(ValueProvider.get_email())
        # LoginModal(self.driver).click_next_button_first()
        # LoginModal(self.driver).set_password(ValueProvider.get_password())
        # LoginModal(self.driver).click_next_button_second()
        time.sleep(5)
        print('Check the number', flush=True)
        try:
            number = LoginModal(self.driver).aouth_number_txt()
            print(number, flush=True)
        except:
            print('Number has not been generated', flush=True)
        time.sleep(20)

        try:
            number = LoginModal(self.driver).aouth_number_txt()
            print(number, flush=True)
        except:
            print('No more number', flush=True)

        time.sleep(20)

        try:
            number = LoginModal(self.driver).aouth_number_txt()
            print(number, flush=True)
        except:
            print('No more number', flush=True)
        time.sleep(20)
        screenshot_path = os.path.join(os.getcwd(), 'artifacts/screenshots', f'{self.id()}.png')
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        self.driver.save_screenshot(screenshot_path)
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        self.driver.maximize_window()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()