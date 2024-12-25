from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from SLP.ui.Elements.base_element import BaseElement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select as SeleniumSelect

SELECT = (By.XPATH, ".")


class Select(BaseElement):
    def __init__(self, node: WebElement):
        super().__init__(node)
        self.select_element = None
        self._select = None

    def get_select_loc(self):
        if not self._select:
            self._select = SeleniumSelect(self.node.find_element(*SELECT))
        return self._select



    def get_options(self):
        return self.get_select_loc().options

    def set_select(self, source):
        return self.get_select_loc().select_by_value(source)

    def set_select_by_index(self, value):
        return self.get_select_loc().select_by_index(value)

