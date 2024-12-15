from selenium.webdriver.common.by import By

from SLP.ui.Elements.select import Select
from SLP.ui.PageObjects.base_components import BaseComponent

METADATA_SELECT = (By.XPATH, '//*[@id="metadataSelect"]')
COUNTRY = (By.XPATH,'/html/body/section/div/div/div/div[1]/div/form/div[6]/div/div/table/tbody/tr[83]')


class ListComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self.mapper_selector = None
        self._source_selected = None

    def get_list_metadata_select(self):
        node = self.node.find_element(*METADATA_SELECT)
        self._source_selected = Select(node)
        return self._source_selected

    def get_metadata_number(self):
        elements = self.get_list_metadata_select().get_options()
        return len(elements)

    def list_metadata_select(self, metadata):
        return self.get_list_metadata_select().set_select_by_index(metadata)

    def get_map_filed(self, xpath):
        return self.node.find_element(*xpath)

    def get_list_address_country(self):
        return self.node.find_element(*COUNTRY)

    def get_txt_list_address_country(self):
        return self.get_list_address_country().text





