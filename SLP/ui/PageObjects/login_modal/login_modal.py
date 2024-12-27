from selenium.webdriver.common.by import By
from SLP.ui.Elements.button import Button
from SLP.ui.Elements.input import Input
from SLP.ui.PageObjects.base_components import BaseComponent

GOOGLE_USER = (By.XPATH, '//*[@id="identifierId"]')
NEXT_BTN_FIRST = (By.XPATH, '//*[@id="identifierNext"]/div/button')
NEXT_BTN_SECOND = (By.XPATH, '//*[@id="passwordNext"]/div/button')
PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
GOOGLE_BUTTON = (By.CSS_SELECTOR, '#gb > div > div.gb_Re > a')


class LoginModal(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._google_account_btn = None
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

    def google_account_btn(self):
        node = self.node.find_element(*GOOGLE_BUTTON)
        self._google_account_btn = Button(node)
        return self._google_account_btn

    def google_account_btn_click(self):
        self.google_account_btn().click_button()



