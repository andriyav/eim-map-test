from selenium.webdriver.common.by import By
from SLP.ui.Elements.base_element import BaseElement
from selenium.webdriver.remote.webelement import WebElement

INPUT = (By.XPATH, ".")


class Input(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._input = None

    def get_input(self):
        if not self._input:
            self._input = self.node.find_element(*INPUT)
        return self._input

    def set_text(self, text):
        self.get_input().send_keys(text)
