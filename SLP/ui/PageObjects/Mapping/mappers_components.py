import time
from selenium.webdriver.common.by import By
from SLP.ui.Elements.input import Input
from SLP.ui.Elements.select import Select
from SLP.ui.PageObjects.base_components import BaseComponent
from tests.value_provider import ValueProvider

ELEMENT_MAPPER = (By.CSS_SELECTOR, "#foo")
MAPPER_JSON_PATH = (By.CSS_SELECTOR, "#jsonform-3-elt-json_path")
MAPPER_CREATE_BTN = (By.CSS_SELECTOR, "#addForm > div > input")


class MappersComponents(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._json_path_input = None
        self._element_selected = None
        self.mapper_selector = None

    def get_mapper_selector(self):
        general_selector = ValueProvider.get_mapping_configuration()
        mapper = general_selector["field"]
        return self.node.find_element(By.CSS_SELECTOR,
                                      f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.{mapper} > td:nth-child(2) > div > span")

    def mapper_selector_click(self):
        return self.get_mapper_selector().click()

    def get_map_provider(self):
        node = self.node.find_element(*ELEMENT_MAPPER)
        self._element_selected = Select(node)
        return self._element_selected

    def select_map_provider(self, provider):
        return self.get_map_provider().set_select_by_index(provider)

    def get_mapper_json_path(self):
        if not self._json_path_input:
            node = self.node.find_element(*MAPPER_JSON_PATH)
            self._json_path_input = Input(node)
        return self._json_path_input

    def set_json_path_value(self):
        json_path_value = ValueProvider.get_mapping_configuration()
        mapper = json_path_value["Metadata"]
        return self.get_mapper_json_path().set_text_in(mapper)

    def get_button_create(self):
        return self.node.find_element(*MAPPER_CREATE_BTN)

    def click_button_create_map(self):
        time.sleep(1)
        return self.get_button_create().click()
