from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from SLP.ui.Elements.select import Select
from SLP.ui.PageObjects.base_components import BaseComponent
from SLP.ui.PageObjects.login_modal.login_modal import LoginModal
APPLY_SOURCE_BTN =(By.XPATH,'//*[@id="applySource"]')
SOURCE_ID = (By.XPATH,'//*[@id="sources"]')


class SourceSelectComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
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





