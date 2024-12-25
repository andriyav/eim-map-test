import time

from selenium.webdriver.common.by import By

from SLP.ui.Elements.select import Select
from SLP.ui.PageObjects.base_components import BaseComponent
from data.value_provider import ValueProvider

ELEMENT_RULE = (By.CSS_SELECTOR, "#foo")
RULE_CREATE_BTN = (By.CSS_SELECTOR, '#addForm > div > input')


class RuleComponents(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._element_selected = None

    def get_rule_selector(self):
        general_selector = ValueProvider.get_mapping_configuration()
        mapper = general_selector["field"]
        return self.node.find_element(By.CSS_SELECTOR,
                                       f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.{mapper} > td:nth-child(4) > div > span")

    def rule_selector_click(self):
        return self.get_rule_selector().click()

    def get_rule_provider(self):
        node = self.node.find_element(*ELEMENT_RULE)
        self._element_selected = Select(node)
        return self._element_selected

    def select_rule_provider(self, provider):
        return self.get_rule_provider().set_select_by_index(provider)

    def get_button_create(self):
        return self.node.find_element(*RULE_CREATE_BTN)

    def click_button_create(self):
        time.sleep(1)
        return self.get_button_create().click()
