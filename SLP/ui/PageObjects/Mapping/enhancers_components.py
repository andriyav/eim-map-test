import time
from selenium.webdriver.common.by import By
from SLP.ui.Elements.select import Select
from SLP.ui.PageObjects.base_components import BaseComponent
from tests.value_provider import ValueProvider

ELEMENT_ENHANCER = (By.CSS_SELECTOR, "#foo")
ENHANCER_CREATE_BTN = (By.CSS_SELECTOR, '#addForm > div > input')


class EnhancerComponents(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._json_path_input = None
        self._element_selected = None

    def get_enhancer_selector(self):
        general_selector = ValueProvider.get_mapping_configuration()
        mapper = general_selector["field"]
        return self.node.find_element(By.CSS_SELECTOR,
                                      f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.{mapper} > td:nth-child(4) > div > span")

    def enhancer_selector_click(self):
        return self.get_enhancer_selector().click()

    def get_enhancer_provider(self):
        node = self.node.find_element(*ELEMENT_ENHANCER)
        self._element_selected = Select(node)
        return self._element_selected

    def select_enhancer_provider(self, provider):
        return self.get_enhancer_provider().set_select_by_index(provider)

    def get_button_create(self):
        return self.node.find_element(*ENHANCER_CREATE_BTN)

    def click_button_create(self):
        return self.get_button_create().click()
