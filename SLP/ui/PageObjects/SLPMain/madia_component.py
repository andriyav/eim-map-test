from selenium.webdriver.common.by import By

from SLP.ui.Elements.select import Select
from SLP.ui.PageObjects.base_components import BaseComponent

METADATA_SELECT = (By.XPATH, '//*[@id="metadataSelect"]')
PH_TYPE_FIELD = (
By.CSS_SELECTOR, '#nav-home > div > table > tbody > tr.master_schema.kw_photo.required.photos-items-properties-ph_category')


class MediaComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self.mapper_selector = None
        self._source_selected = None

    def get_map_filed(self, xpath):
        return self.node.find_element(*xpath)

    def get_ph_type(self):
        return self.node.find_element(*PH_TYPE_FIELD)

    def get_txt_ph_type(self):
        return self.get_ph_type().text
