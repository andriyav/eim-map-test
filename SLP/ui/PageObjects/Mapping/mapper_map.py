import time

from selenium.webdriver.common.by import By

from SLP.ui.PageObjects.Mapping.mappers_components import MappersComponents
from SLP.ui.PageObjects.SLPMain.listing_component import ListComponent
from SLP.ui.PageObjects.SLPMain.slp_main import SLPMain

IMPLIS_WAIT_MAP = (By.CSS_SELECTOR, '#listing_mapper_list_category__0')


class MapperMap:
    def __init__(self, driver):
        self.driver = driver

    def mapper_map(self, mapper_provider):
        self.driver.implicitly_wait(10)
        SLPMain(self.driver).impl_wait_metadata()
        MappersComponents(self.driver).mapper_selector_click()
        MappersComponents(self.driver).select_map_provider(mapper_provider)
        MappersComponents(self.driver).set_json_path_value()
        time.sleep(1)
        MappersComponents(self.driver).click_button_create()
        SLPMain(self.driver).click_save_button_()
        SLPMain(self.driver).click_OK_button_()

