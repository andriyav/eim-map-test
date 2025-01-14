import os
import time
import unittest
from selenium import webdriver
from SLP.ui.PageObjects.SLPlogin.slp_login import LoginComponent
from data.value_provider import ValueProvider

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
        self.driver.maximize_window()

        screenshot_path = os.path.join(os.getcwd(), 'artifacts/screenshots', f'{self.id()}.png')
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        self.driver.save_screenshot(screenshot_path)
        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        self.driver.maximize_window()
        time.sleep(5)

    def _login(self):
        self.driver.implicitly_wait(10)
        LoginComponent(self.driver).click_authorisation_btn()

    def tearDown(self):
        self.driver.quit()