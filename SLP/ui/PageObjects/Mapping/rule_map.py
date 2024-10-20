import time

from selenium.webdriver.common.by import By

from SLP.ui.PageObjects.Mapping.mappers_components import MappersComponents
from SLP.ui.PageObjects.Mapping.rule_components import RuleComponents
from SLP.ui.PageObjects.SLPMain.listing_component import ListComponent
from SLP.ui.PageObjects.SLPMain.slp_main import SLPMain

IMPLIS_WAIT_MAP = (By.CSS_SELECTOR, '#listing_mapper_list_category__0')


class RuleMap:
    def __init__(self, driver):
        self.driver = driver

    def rule_map(self, mapper_provider):
        self.driver.implicitly_wait(20)
        SLPMain(self.driver).impl_wait_metadata()
        RuleComponents(self.driver).rule_selector_click()
        RuleComponents(self.driver).select_rule_provider(mapper_provider)
        time.sleep(1)
        RuleComponents(self.driver).click_button_create()

