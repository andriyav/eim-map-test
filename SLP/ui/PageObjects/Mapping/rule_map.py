from selenium.webdriver.common.by import By

from SLP.ui.PageObjects.Mapping.mappers_components import MappersComponents
from SLP.ui.PageObjects.SLPMain.listing_component import ListComponent
from SLP.ui.PageObjects.SLPMain.slp_main import SLPMain

IMPLIS_WAIT_MAP = (By.CSS_SELECTOR, '#listing_mapper_list_category__0')


class RuleMap:
    def __init__(self, driver):
        self.driver = driver

    def rule_map(self, mapper_provider):
        pass
