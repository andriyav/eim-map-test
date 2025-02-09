from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import wait

from SLP.ui.Elements.select import Select
from SLP.ui.PageObjects.base_components import BaseComponent
from SLP.ui.PageObjects.login_modal.login_modal import LoginModal
APPLY_SOURCE_BTN =(By.XPATH,'//*[@id="applySource"]')
SOURCE_ID = (By.ID, 'sources')
SOURCE_SELECT = (By.CSS_SELECTOR, '#navbarDropdown')
SOURCE_IN_BUTTON = (By.CSS_SELECTOR,
                    '#navbarNav > ul.navbar-nav.ml-auto.mb-2.mb-lg-0 > li > ul > li.nav-item.dropdown > a')


class SourceSelectComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._select_element = None
        self._source_selected = None

    def get_apply_source_btn(self) -> WebElement:
        return self.node.find_element(*APPLY_SOURCE_BTN)

    def click_apply_source_btn(self):
        self.get_apply_source_btn().click()
        return LoginModal(self.node)

    def get_source_select(self):
        node = self.node.find_element(*SOURCE_ID)
        self._source_selected = Select(node)
        return self._source_selected


    def source_select(self, source):
        return self.get_source_select().set_select(source)

    def get_source_button(self):
        return self.node.find_element(*SOURCE_SELECT)

    def click_source_button(self):
        self.get_source_button().click()

    def get_in_source_button(self):
        return self.node.find_element(*SOURCE_IN_BUTTON)

    def click_in_source_button(self):
        self.get_in_source_button().click()

    def get_select_wait(self):
        if not self._select_element:
            self._select_element = wait.WebDriverWait(self.node.find_element(*SOURCE_ID), 10)
        return self._select_element




