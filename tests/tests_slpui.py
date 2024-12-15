import time

from parameterized import parameterized
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from SLP.test_data import sources
from SLP.ui.PageObjects.Mapping.mapping import Mapping
from SLP.ui.PageObjects.SLPMain.listing_component import ListComponent
from SLP.ui.PageObjects.SLPMain.slp_main import SLPMain
from SLP.ui.PageObjects.SLPMain.source_select_component import SourceSelectComponent
from tests.test_runner import BaseTestRunner
from selenium.webdriver.support import expected_conditions as EC

PHOTO_TAB = (By.XPATH, "/html/body/section/div/div/div/div[1]/div/div/a[2]")
IS_SHORT_SALE = (By.CSS_SELECTOR, '#nav-home > div > table > tbody > tr.master_schema.kw_listing.is_short_sale')
IMPLIS_WAIT_MAP = (By.CSS_SELECTOR, '#listing_mapper_list_category__0')
SOURCE_ID = (By.XPATH,'//*[@id="sources"]')
GOLDEN_VALUE = '''is_short_sale
+
[add]
ValueProvider(json_path=SpecialListingConditions,skip_values=[])
[add]
[add]
Is_Short_Sale()
[add]'''


class SLPPageTestCase(BaseTestRunner):

    @parameterized.expand(sources)
    def test_map_validation(self, source):
        self.driver.implicitly_wait(20)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        print(metadata_numbers)
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                SLPMain(self.driver).metadata_main_select(metadata)
                Mapping(self.driver).mapping()
                SLPMain(self.driver).scroll_top()
                SourceSelectComponent(self.driver).get_select_wait().until(EC.visibility_of_element_located(PHOTO_TAB))
                SLPMain(self.driver).select_photo_tub()
                SLPMain(self.driver).select_list_tub()
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                ListComponent(self.driver).get_map_filed(IS_SHORT_SALE)
                actual = ListComponent(self.driver).get_map_filed(IS_SHORT_SALE).text
                # Map restart to reset locator
                SourceSelectComponent(self.driver).click_source_button()
                SourceSelectComponent(self.driver).click_in_source_button()
                SourceSelectComponent(self.driver).get_select_wait().until(EC.visibility_of_element_located(SOURCE_ID))
                SLPMain(self.driver).source_select(source)
                SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
                self.assertEqual(actual, GOLDEN_VALUE)



    # def test_map_get_golden(self, source='80'):
    #     self.driver.implicitly_wait(20)
    #
    #     SLPMain(self.driver).source_select(source)
    #     SLPMain(self.driver).metadata_main_select(1)
    #     SLPMain(self.driver).impl_wait_metadata()
    #     text = MapValueComponents(self.driver).text_value_selector()
    #     print(text)
