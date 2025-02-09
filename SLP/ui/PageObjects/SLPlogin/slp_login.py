from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SLP.ui.PageObjects.base_components import BaseComponent
from SLP.ui.PageObjects.login_modal.login_modal import LoginModal
LOGIN_WITH_GOOGLE = (By.XPATH,'//*[@id="nav-home"]/div/table/tbody/tr[2]/td/div/input')


class LoginComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)

    def get_authorisation_btn(self) -> WebElement:
        return self.node.find_element(*LOGIN_WITH_GOOGLE)

    def click_authorisation_btn(self):
        self.get_authorisation_btn().click()
        return LoginModal(self.node)

