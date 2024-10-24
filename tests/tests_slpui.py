import time

from selenium.webdriver.common.by import By

from SLP.ui.PageObjects.Mapping.mapping import Mapping
from SLP.ui.PageObjects.SLPMain.listing_component import ListComponent
from SLP.ui.PageObjects.SLPMain.slp_main import SLPMain
from tests.test_runner import BaseTestRunner

PHOTO_TAB = (By.XPATH, "/html/body/section/div/div/div/div[1]/div/div/a[2]")
IS_SHORT_SALE = (By.CSS_SELECTOR, '#nav-home > div > table > tbody > tr.master_schema.kw_listing.is_short_sale')
IMPLIS_WAIT_MAP = (By.CSS_SELECTOR, '#listing_mapper_list_category__0')


class SLPPageTestCase(BaseTestRunner):

    def test_map_validation(self):
        """ Mapping Test"""
        self.driver.implicitly_wait(20)
        SLPMain(self.driver).source_select()
        SLPMain(self.driver).metadata_main_select()
        Mapping(self.driver).mapping()
        SLPMain(self.driver).scroll_top()
        SLPMain(self.driver).select_photo_tub()
        SLPMain(self.driver).select_list_tub()
        SLPMain(self.driver).metadata_main_select()
        SLPMain(self.driver).impl_wait_metadata()
        ListComponent(self.driver).get_map_filed(IS_SHORT_SALE)
        text_field = ListComponent(self.driver).get_map_filed(IS_SHORT_SALE).text
        self.assertEqual(
            'is_short_sale\n'
            '+\n'
            '[add]\n'
            'ValueProvider(json_path=SpecialListingConditions,skip_values=[])\n'
            '[add]\n'
            '[add]\n'
            'Is_Short_Sale()\n'
            '[add]', text_field)
