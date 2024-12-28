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

    # def _init_driver(self):
        chrome_options = webdriver.ChromeOptions()
    #     chrome_options.add_argument('--disable-gpu')
    #     chrome_options.add_argument('--no-sandbox')
    #     chrome_options.add_argument('--disable-dev-shm-usage')
    #     chrome_options.add_argument('--disable-popup-blocking')
    #     chrome_options.add_argument('--window-size=1920x1080')
        chrome_options.add_argument(f"user-data-dir={CHROME_USER_DIR}")
        chrome_options.add_argument("profile-directory=Default")
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
        LoginModal(self.driver).set_email(ValueProvider.get_email())
        LoginModal(self.driver).click_next_button_first()
        LoginModal(self.driver).set_password(ValueProvider.get_password())
        LoginModal(self.driver).click_next_button_second()
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
        # LoginModal(self.driver).click_get_recovery_btn()
        # time.sleep(5)
        # LoginModal(self.driver).click_recovery_next_btn()
        # time.sleep(5)
        # LoginModal(self.driver).set_last_password('Components12!')
        # LoginModal(self.driver).click_get_last_psw_next_btn()
        screenshot_path = os.path.join(os.getcwd(), 'artifacts/screenshots', f'{self.id()}.png')
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        self.driver.save_screenshot(screenshot_path)

        with open("page_source.html", "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        # LoginModal(self.driver).click_get_try_another_btn()
        self.driver.maximize_window()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()