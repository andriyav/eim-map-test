from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from SLP.ui.Elements.base_element import BaseElement

TUB = (By.XPATH, ".")


class Tub(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self._tub = None


    def get_tab(self):
        if not self._tub:
            self._tub = self.node.find_element(*TUB)
        return self._tub

    def select_tab(self):
        self.get_tab().click()
