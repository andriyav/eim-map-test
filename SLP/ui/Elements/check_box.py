from selenium.webdriver.remote.webelement import WebElement
from SLP.ui.Elements.base_element import BaseElement


class CheckBox(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)

    def get_check_box(self):
        return self.node

    def select_check_box(self):
        self.get_check_box().click()

