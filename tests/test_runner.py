import os
import time
import unittest
from selenium import webdriver
from SLP.ui.PageObjects.SLPlogin.slp_login import LoginComponent
from SLP.ui.PageObjects.login_modal.login_modal import LoginModal
from data.value_provider import ValueProvider

# CHROME_USER_DIR = "/home/runner/work/SLPUI/SLPUI/SLPUI/data/cash1"
# CHROME_USER_DIR = os.path.abspath("./SLPUI/data/cash2")

CHROME_USER_DIR = "/home/runner/work/SLPUI/SLPUI/tests/SLPUI/cash"

IMPLICITLY_WAIT = 10


class BaseTestRunner(unittest.TestCase):

    def _take_screenshot(self, filename='screenshot.png'):
        os.makedirs('./artifacts/screenshots', exist_ok=True)
        self.driver.save_screenshot(f'./artifacts/screenshots/{filename}')

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self._init_driver()
        self._login()

    def _init_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument('--window-size=1920x1080')
        chrome_options.add_argument(f"user-data-dir={CHROME_USER_DIR}")
        chrome_options.add_argument("profile-directory=Default")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.driver.get(ValueProvider.get_base_url())
        # LoginComponent(self.driver).click_authorisation_btn()
        # LoginModal(self.driver).set_email(ValueProvider.get_email())
        # LoginModal(self.driver).click_next_button_first()
        # LoginModal(self.driver).set_password(ValueProvider.get_password())
        # LoginModal(self.driver).click_next_button_second()
        self.driver.maximize_window()
        # time.sleep(5)
        self._take_screenshot('button_interaction_failed.png')
        # time.sleep(60)
        print(f"Resolved CHROME_USER_DIR path: {os.path.abspath(CHROME_USER_DIR)}")
        print(f"Resolved CHROME_USER_DIR path: {os.path.abspath('~/.config/google-chrome/Default')}")


    def _login(self):
        self.driver.implicitly_wait(10)
        LoginComponent(self.driver).click_authorisation_btn()
        self.driver.maximize_window()



    '''Login with username and password'''

    # def _init_driver(self):
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument('--disable-gpu')
    #     chrome_options.add_argument('--no-sandbox')
    #     chrome_options.add_argument('--disable-dev-shm-usage')
    #     chrome_options.add_argument('--disable-popup-blocking')
    #     chrome_options.add_argument('--window-size=1920x1080')
    #     self.driver = webdriver.Chrome(options=chrome_options)
    #     self.driver.implicitly_wait(IMPLICITLY_WAIT)
    #     self.driver.maximize_window()
    #     self.driver.get(ValueProvider.get_base_url())
    #
    # def _login(self):
    #     self.driver.implicitly_wait(10)
    #     LoginComponent(self.driver).click_authorisation_btn()
    #     LoginModal(self.driver).set_email(ValueProvider.get_email())
    #     LoginModal(self.driver).click_next_button_first()
    #     LoginModal(self.driver).set_password(ValueProvider.get_password())
    #     LoginModal(self.driver).click_next_button_second()
    #     self.driver.maximize_window()
    #     time.sleep(5)

    def tearDown(self):
        self.driver.quit()