import time
from SLP.ui.PageObjects.Mapping.mapper_map import MapperMap
from SLP.ui.PageObjects.Mapping.rule_map import RuleMap
from SLP.ui.base_page import SLPMain
from data.value_provider import ValueProvider


class Mapping:
    def __init__(self, driver):
        self.driver = driver

    def mapping(self):
        mapper_provider = ValueProvider.get_mapping_configuration()["MappersProvider"]
        rule_provider = ValueProvider.get_mapping_configuration()["Rules"]
        if mapper_provider:
            MapperMap(self.driver).mapper_map(mapper_provider)
        if rule_provider:
            RuleMap(self.driver).rule_map(rule_provider)
        SLPMain(self.driver).click_save_button_()
        SLPMain(self.driver).click_OK_button_()
        time.sleep(3)



