import os
import time
import unittest
from selenium import webdriver
from SLP.ui.PageObjects.SLPlogin.slp_login import LoginComponent
from SLP.ui.PageObjects.login_modal.login_modal import LoginModal
from data.value_provider import ValueProvider
from selenium.webdriver.chrome.options import Options

CHROME_USER_DIR = "C:/Users/aandrusy/AppData/Local/Google/Chrome/UserData/aandrusy"
IMPLICITLY_WAIT = 10
from pyvirtualdisplay import Display
# Start a virtual display if not already running (useful for CI environments)
if os.environ.get("CI"):  # Check if running in CI
    display = Display(visible=False, size=(1920, 1080))
    display.start()
    import pyautogui
else:
    import pyautogui

import os
import unittest

class MyTest(unittest.TestCase):
    @unittest.skipUnless(os.getenv("DISPLAY"), "Requires a graphical display")
    def test_gui_functionality(self):
        # GUI-dependent test
        pass

class BaseTestRunner(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self._init_driver()
        self._login()

    # def _init_driver(self):
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument(f"user-data-dir={CHROME_USER_DIR}")
    #     chrome_options.add_argument("profile-directory=Default")
    #     self.driver = webdriver.Chrome(options=chrome_options)
    #     self.driver.implicitly_wait(IMPLICITLY_WAIT)
    #     self.driver.get(ValueProvider.get_base_url())

    # def _login(self):
    #     self.driver.implicitly_wait(10)
    #     LoginComponent(self.driver).click_authorisation_btn()
    #     self.driver.maximize_window()

    """Login with username and password"""

    def _init_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.driver.maximize_window()
        self.driver.get(ValueProvider.get_base_url())

    def _login(self):
        self.driver.implicitly_wait(10)
        LoginComponent(self.driver).click_authorisation_btn()
        LoginModal(self.driver).set_email(ValueProvider.get_email())
        LoginModal(self.driver).click_next_button_first()
        LoginModal(self.driver).set_password(ValueProvider.get_password())
        LoginModal(self.driver).click_next_button_second()
        self.driver.maximize_window()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

