from parameterized import parameterized
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from data.test_data import sources
from SLP.ui.PageObjects.Mapping.mapping import Mapping
from SLP.ui.PageObjects.SLPMain.listing_component import ListComponent
from SLP.ui.PageObjects.SLPMain.slp_main import SLPMain
from SLP.ui.PageObjects.SLPMain.source_select_component import SourceSelectComponent
from tests.test_runner import BaseTestRunner
from selenium.webdriver.support import expected_conditions as EC
SOURCE_ID = (By.XPATH, '//*[@id="sources"]')
COUNTRY = '''list_address.properties.country
+
[add]
[add]
[add]
[add]
SetConstant(const=US,const_type=str)'''


class TestPromotionChecklist(BaseTestRunner):

    @parameterized.expand(sources)
    def test_list_address_properties_country(self, source):
        self.driver.implicitly_wait(20)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                ListComponent(self.driver).get_list_address_country()
                actual = ListComponent(self.driver).get_txt_list_address_country()
                self.assertEqual(COUNTRY, actual)
