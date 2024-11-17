import time

from selenium.webdriver.common.by import By

from SLP.ui.PageObjects.Mapping.mappers_components import MappersComponents, MAPPER_CREATE_BTN
from SLP.ui.PageObjects.SLPMain.listing_component import ListComponent
from SLP.ui.PageObjects.SLPMain.slp_main import SLPMain
from SLP.ui.PageObjects.SLPMain.source_select_component import SourceSelectComponent
from selenium.webdriver.support import expected_conditions as EC
IMPLIS_WAIT_MAP = (By.CSS_SELECTOR, '#listing_mapper_list_category__0')
IMPLIS_WAIT = (By.CSS_SELECTOR, '#addModal > div > div > div.modal-body')


class MapperMap:
    def __init__(self, driver):
        self.driver = driver

    def mapper_map(self, mapper_provider):
        self.driver.implicitly_wait(10)
        SLPMain(self.driver).impl_wait_metadata()
        MappersComponents(self.driver).mapper_selector_click()
        MappersComponents(self.driver).select_map_provider(mapper_provider)
        MappersComponents(self.driver).set_json_path_value()
        # time.sleep(1)
        MappersComponents(self.driver).click_button_create()
        # SourceSelectComponent(self.driver).get_select_wait().until(
        #     EC. invisibility_of_element_located(IMPLIS_WAIT))




