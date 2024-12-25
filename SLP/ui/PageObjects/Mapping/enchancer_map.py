import time
from selenium.webdriver.common.by import By
from SLP.ui.PageObjects.Mapping.enhancers_components import EnhancerComponents
from SLP.ui.PageObjects.Mapping.rule_components import RuleComponents
from SLP.ui.PageObjects.SLPMain.slp_main import SLPMain

IMPLIS_WAIT_MAP = (By.CSS_SELECTOR, '#listing_mapper_list_category__0')


class EnhancerMap:
    def __init__(self, driver):
        self.driver = driver

    def enhancer_map(self, enhancer_provider):
        self.driver.implicitly_wait(20)
        SLPMain(self.driver).impl_wait_metadata()
        EnhancerComponents(self.driver).enhancer_selector_click()
        EnhancerComponents(self.driver).select_enhancer_provider(enhancer_provider)
        RuleComponents(self.driver).click_button_create()

