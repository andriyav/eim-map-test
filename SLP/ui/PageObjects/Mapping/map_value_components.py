from selenium.webdriver.common.by import By
from SLP.ui.PageObjects.base_components import BaseComponent
from data.value_provider import ValueProvider

ELEMENT_MAPPER = (By.CSS_SELECTOR, "#foo")
MAPPER_JSON_PATH = (By.CSS_SELECTOR, "#jsonform-3-elt-json_path")
MAPPER_CREATE_BTN = (By.CSS_SELECTOR, "#addForm > div > input")

''' Retrieve the gold standard value of the field for comparison with the actual value in the test'''


class MapValueComponents(BaseComponent):
    def __init__(self, node):
        super().__init__(node)

    def get_map_value_selector(self):
        general_selector = ValueProvider.get_mapping_configuration()
        mapper = general_selector["field"]
        return self.node.find_element(By.CSS_SELECTOR,
                                      f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.{mapper}"
                                      )

    def text_value_selector(self):
        return self.get_map_value_selector().text
