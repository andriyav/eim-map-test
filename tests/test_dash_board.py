import time
from parameterized import parameterized
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from SLP.test_data import sources
from SLP.ui.PageObjects.DashBoard.dash_board import DashBoard
from SLP.ui.PageObjects.RawData.raw_data import RawData
from SLP.ui.PageObjects.SLPMain.slp_main import SLPMain
from SLP.ui.PageObjects.SLPMain.source_select_component import SourceSelectComponent
from tests.test_runner import BaseTestRunner
from selenium.webdriver.support import expected_conditions as EC

SOURCE_ID = (By.XPATH, '//*[@id="sources"]')


class SLPPageTestCase(BaseTestRunner):

    @parameterized.expand(sources)
    def test_dashboard_source_number(self, source):
        # go to dashboard
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
        SLPMain(self.driver).mls_btn_click()
        SLPMain(self.driver).ld_btn_click()
        DashBoard(self.driver).set_kw_source_id(source)
        DashBoard(self.driver).click_submit_btn()
        actual = DashBoard(self.driver).get_source_id_txt()
        # Check if the source mls_id on the board matches the loaded source.
        self.assertEqual(actual, source)

    @parameterized.expand(sources)
    def test_dashboard_media_oh(self, source):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
        SLPMain(self.driver).mls_btn_click()
        SLPMain(self.driver).ld_btn_click()
        DashBoard(self.driver).set_kw_source_id(source)
        DashBoard(self.driver).click_submit_btn()
        DashBoard(self.driver).select_photo_check_box()
        DashBoard(self.driver).select_oh_check_box()
        # Check that the open house and media records are displayed on the dashboard.
        try:
            DashBoard(self.driver).get_source_id_txt()
            result = True
        except:
            result = False
        self.assertTrue(result)

    @parameterized.expand(sources)
    def test_sold_data(self, source):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
        SLPMain(self.driver).mls_btn_click()
        SLPMain(self.driver).ld_btn_click()
        DashBoard(self.driver).set_kw_source_id(source)
        DashBoard(self.driver).click_submit_btn()
        rows = DashBoard(self.driver).get_list_of_sources()
        n = 0
        result = False
        # check if the sold listings are shown on the dashboard.
        for row in rows:
            n += 1
            # Check if the row contains a "td" with the text "Sold"
            print(n)
            # print(row.text)
            if 'Sold' in row.text:
                result = True
                print(n)
                break
        self.assertTrue(result)

    @parameterized.expand(sources)
    def test_market_info(self, source):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
        SLPMain(self.driver).mls_btn_click()
        SLPMain(self.driver).ld_btn_click()
        DashBoard(self.driver).set_kw_source_id(source)
        DashBoard(self.driver).click_submit_btn()
        DashBoard(self.driver).click_view_data_btn()
        RawData(self.driver).click_raw_data_tub()
        display_address = RawData(self.driver).get_marketing_info_collapse('display_address')
        display_internet = RawData(self.driver).get_marketing_info_collapse('display_internet')
        display_list_price = RawData(self.driver).get_marketing_info_collapse('display_list_price')
        display_listing = RawData(self.driver).get_marketing_info_collapse('display_listing')
        display_photo = RawData(self.driver).get_marketing_info_collapse('display_photo')
        # Check that marketing info statuses have values set to true.
        self.assertNotIn(False, (display_address, display_internet, display_list_price, display_listing, display_photo))

    @parameterized.expand(sources)
    def test_media_count(self, source):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
        SLPMain(self.driver).mls_btn_click()
        SLPMain(self.driver).ld_btn_click()
        DashBoard(self.driver).set_kw_source_id(source)
        DashBoard(self.driver).select_photo_check_box()
        DashBoard(self.driver).click_submit_btn()
        kw_id_txt = DashBoard(self.driver).get_kw_id_txt()
        DashBoard(self.driver).set_kwid(kw_id_txt)
        DashBoard(self.driver).click_submit_btn()
        DashBoard(self.driver).click_view_data_btn_single()
        RawData(self.driver).click_raw_data_tub__single()
        photo_number = RawData(self.driver).get_photo_number()
        media_count = RawData(self.driver).get_photo_count()
        # Check that values of media_count filed is equal to the number of elements in the list of photo filed.
        self.assertEqual(media_count, photo_number)
