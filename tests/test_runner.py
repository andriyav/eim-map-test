import os
import pickle
import time
import unittest
from selenium import webdriver
from SLP.ui.PageObjects.SLPlogin.slp_login import LoginComponent
from SLP.ui.PageObjects.login_modal.login_modal import LoginModal
from data.value_provider import ValueProvider

CHROME_USER_DIR = '/home/runner/.config/google-chrome/'
# CHROME_USER_DIR = os.path.abspath("./SLPUI/data/cash2")

IMPLICITLY_WAIT = 10


class BaseTestRunner(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        self._init_driver()
        self._login()

    # def _init_driver(self):
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument('--disable-gpu')
    #     chrome_options.add_argument('--no-sandbox')
    #     chrome_options.add_argument('--disable-dev-shm-usage')
    #     chrome_options.add_argument('--disable-popup-blocking')
    #     chrome_options.add_argument('--window-size=1920x1080')
    #     chrome_options.add_argument(f"user-data-dir={CHROME_USER_DIR}")
    #     chrome_options.add_argument("profile-directory=Default")
    #     self.driver = webdriver.Chrome(options=chrome_options)
    #     self.driver.implicitly_wait(IMPLICITLY_WAIT)
    #     self.driver.get(ValueProvider.get_base_url())
    #     print(f"Resolved CHROME_USER_DIR path: {os.path.abspath(CHROME_USER_DIR)}")
    #
    # def _login(self):
    #     self.driver.implicitly_wait(10)
    #     LoginComponent(self.driver).click_authorisation_btn()
    #     self.driver.maximize_window()



    '''Login with username and password'''

    def _init_driver(self):
        with open("cookies.pkl", "rb") as cookie_file:
            cookies = pickle.load(cookie_file)
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument(f"user-data-dir={CHROME_USER_DIR}")
        # chrome_options.add_argument("profile-directory=Default")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.driver.maximize_window()
        self.driver.get(ValueProvider.get_google_url())
        time.sleep(5)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.get(ValueProvider.get_google_url())
        self.driver.get(ValueProvider.get_base_url())

    def _login(self):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        LoginComponent(self.driver).click_authorisation_btn()
        LoginModal(self.driver).set_email(ValueProvider.get_email())
        LoginModal(self.driver).click_next_button_first()
        LoginModal(self.driver).set_password(ValueProvider.get_password())
        LoginModal(self.driver).click_next_button_second()
        self.driver.implicitly_wait(10)
        time.sleep(10)

        time.sleep(10)
        # cookies = self.driver.get_cookies()
        # with open("cookies.pkl", "wb") as cookie_file:
        #     pickle.dump(cookies, cookie_file)
        time.sleep(3)
        screenshot_path = os.path.join(os.getcwd(), 'artifacts/screenshots', f'{self.id()}.png')
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        self.driver.save_screenshot(screenshot_path)
        self.driver.maximize_window()
        self.driver.get(ValueProvider.get_base_url())
        time.sleep(5)
        # with open("page_source.html", "w", encoding="utf-8") as f:
        #     f.write(self.driver.page_source)
        # self.driver.get(ValueProvider.get_base_url())
        # LoginComponent(self.driver).click_authorisation_btn()

    def tearDown(self):
        self.driver.quit()