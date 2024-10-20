import time

from selenium.webdriver.common.by import By

from SLP.ui.Elements.select import Select
from SLP.ui.PageObjects.base_components import BaseComponent
from tests.value_provider import ValueProvider

METADATA_SELECT = (By.XPATH, '//*[@id="metadataSelect"]')


class ListComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self.mapper_selector = None
        self._source_selected = None

    def get_list_metadata_select(self):
        node = self.node.find_element(*METADATA_SELECT)
        self._source_selected = Select(node)
        return self._source_selected

    def list_metadata_select(self, metadata=1):
        return self.get_list_metadata_select().set_select_by_index(metadata)

    def get_map_filed(self, xpath):
        return self.node.find_element(*xpath)





