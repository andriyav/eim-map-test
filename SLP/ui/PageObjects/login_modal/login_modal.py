from selenium.webdriver.common.by import By
from SLP.ui.Elements.button import Button
from SLP.ui.Elements.input import Input
from SLP.ui.PageObjects.base_components import BaseComponent

GOOGLE_USER = (By.XPATH, '//*[@id="identifierId"]')
NEXT_BTN_FIRST = (By.XPATH, '//*[@id="identifierNext"]/div/button')
NEXT_BTN_SECOND = (By.XPATH, '//*[@id="passwordNext"]/div/button')
PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
RECOVERY_ACCOUNT_BTN = (By.CSS_SELECTOR, '#accountRecoveryButton > div > div > a')
RECOVERY_NEXT_BTN = (By.CSS_SELECTOR, '#identifierNext > div > button')
LAST_PSW_INPUT = (By.CSS_SELECTOR, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
LAST_PSW_BTN = (By.CSS_SELECTOR, '#passwordNext > div > button')
TRY_ANOTHER_WAY = (By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div.JYXaTc > div > div.FO2vFd > div > div > button')


class LoginModal(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._get_try_another_btn = None
        self._get_last_psw_next_btn = None
        self._last_password_input = None
        self._recovery_next_btn = None
        self._get_recovery_btn = None
        self._email_input = None
        self._password_input = None
        self._login_button_first = None
        self._login_button_second = None

    def get_email_input(self):
        node = self.node.find_element(*GOOGLE_USER)
        self._email_input = Input(node)
        return self._email_input

    def set_email(self, email: str):
        self.get_email_input().set_text(email)
        return self

    def get_next_button_first(self):
        node = self.node.find_element(*NEXT_BTN_FIRST)
        self._login_button_first = Button(node)
        return self._login_button_first

    def click_next_button_first(self):
        self.get_next_button_first().click_button()

    def get_password_input(self):
        if not self._password_input:
            node = self.node.find_element(*PASSWORD_INPUT)
            self._password_input = Input(node)
        return self._password_input

    def set_password(self, password: str):
        self.get_password_input().set_text(password)
        return self

    def get_next_button_second(self):
        node = self.node.find_element(*NEXT_BTN_SECOND)
        self._login_button_second = Button(node)
        return self._login_button_second

    def click_next_button_second(self):
        self.get_next_button_second().click_button()

    def get_recovery_btn(self):
        node = self.node.find_element(*RECOVERY_ACCOUNT_BTN)
        self._get_recovery_btn = Button(node)
        return self._get_recovery_btn

    def click_get_recovery_btn(self):
        self.get_recovery_btn().click_button()

    def get_recovery_next_btn(self):
        node = self.node.find_element(*RECOVERY_NEXT_BTN)
        self._recovery_next_btn = Button(node)
        return self._recovery_next_btn

    def click_recovery_next_btn(self):
        self.get_recovery_next_btn().click_button()
        
    def get_last_password_input(self):
        if not self._password_input:
            node = self.node.find_element(*LAST_PSW_INPUT)
            self._last_password_input = Input(node)
        return self._last_password_input

    def set_last_password(self, password: str):
        self.get_last_password_input().set_text(password)
        return self

    def get_last_psw_next_btn(self):
        node = self.node.find_element(*LAST_PSW_BTN)
        self._get_last_psw_next_btn = Button(node)
        return self._get_last_psw_next_btn

    def click_get_last_psw_next_btn(self):
        self.get_last_psw_next_btn().click_button()

    def get_try_another_btn(self):
        node = self.node.find_element(*TRY_ANOTHER_WAY)
        self._get_try_another_btn = Button(node)
        return self._get_try_another_btn

    def click_get_try_another_btn(self):
        self.get_try_another_btn().click_button()






