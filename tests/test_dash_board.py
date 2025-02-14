import allure
import pytest
from parameterized import parameterized
from selenium.webdriver.support.wait import WebDriverWait
from data.test_data import sources
from SLP.ui.PageObjects.DashBoard.dash_board import DashBoard, SUBMIT_BTN
from SLP.ui.PageObjects.RawData.raw_data import RawData
from SLP.ui.slp_main import SLPMain
from SLP.ui.PageObjects.SLPMain.source_select_component import SourceSelectComponent, SOURCE_ID
from tests.test_runner import BaseTestRunner
from selenium.webdriver.support import expected_conditions as EC

from utils.db_handler import DBHandler


class SLPPageTestCase(BaseTestRunner):

    @allure.testcase('Test source number validation')
    @parameterized.expand(sources)
    def test_dashboard_source_number(self, source):
        # go to dashboard
        wait = WebDriverWait(self.driver, 20, poll_frequency=0.5, ignored_exceptions=(Exception,))
        wait.until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
        SLPMain(self.driver).mls_btn_click()
        SLPMain(self.driver).ld_btn_click()
        DashBoard(self.driver).set_kw_source_id(source)
        DashBoard(self.driver).click_submit_btn()
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(SUBMIT_BTN))
        actual = DashBoard(self.driver).get_source_id_txt()
        # Check if the source mls_id on the board matches the loaded source.
        self.assertEqual(actual, source)

    @allure.testcase('Check Media and OH availability')
    @parameterized.expand(sources)
    def test_dashboard_media_oh(self, source):
        wait = WebDriverWait(self.driver, 20, poll_frequency=0.5, ignored_exceptions=(Exception,))
        wait.until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
        SLPMain(self.driver).mls_btn_click()
        SLPMain(self.driver).ld_btn_click()
        DashBoard(self.driver).set_kw_source_id(source)
        DashBoard(self.driver).click_submit_btn()
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(SUBMIT_BTN))
        DashBoard(self.driver).select_photo_check_box()
        DashBoard(self.driver).select_oh_check_box()
        # Check that the open house and media records are displayed on the dashboard.
        try:
            DashBoard(self.driver).get_source_id_txt()
            result = True
        except:
            result = False
        self.assertTrue(result)

    @allure.testcase('Test for Sold Data')
    @parameterized.expand(sources)
    def test_sold_data(self, source):
        wait = WebDriverWait(self.driver, 20, poll_frequency=0.5, ignored_exceptions=(Exception,))
        wait.until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
        SLPMain(self.driver).mls_btn_click()
        SLPMain(self.driver).ld_btn_click()
        DashBoard(self.driver).set_kw_source_id(source)
        DashBoard(self.driver).click_submit_btn()
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(SUBMIT_BTN))
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

    @allure.testcase('Test market_info fields')
    @parameterized.expand(sources)
    def test_market_info(self, source):
        wait = WebDriverWait(self.driver, 20, poll_frequency=0.5, ignored_exceptions=(Exception,))
        wait.until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
        SLPMain(self.driver).mls_btn_click()
        SLPMain(self.driver).ld_btn_click()
        DashBoard(self.driver).set_kw_source_id(source)
        DashBoard(self.driver).click_submit_btn()
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(SUBMIT_BTN))
        DashBoard(self.driver).click_view_data_btn()
        RawData(self.driver).click_raw_data_tub()
        display_address = RawData(self.driver).get_marketing_info_collapse('display_address')
        display_internet = RawData(self.driver).get_marketing_info_collapse('display_internet')
        display_list_price = RawData(self.driver).get_marketing_info_collapse('display_list_price')
        display_listing = RawData(self.driver).get_marketing_info_collapse('display_listing')
        display_photo = RawData(self.driver).get_marketing_info_collapse('display_photo')
        # Check that marketing info statuses have values set to true.
        self.assertNotIn(False, (display_address, display_internet, display_list_price, display_listing, display_photo))

    @allure.testcase('Media count test')
    @parameterized.expand(sources)
    def test_media_count(self, source):
        wait = WebDriverWait(self.driver, 20, poll_frequency=0.5, ignored_exceptions=(Exception,))
        wait.until(EC.element_to_be_clickable(SOURCE_ID))
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
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(SUBMIT_BTN))
        DashBoard(self.driver).click_view_data_btn_single()
        RawData(self.driver).click_raw_data_tub__single()
        photo_number = RawData(self.driver).get_photo_number()
        media_count = RawData(self.driver).get_photo_count()
        # Check that values of media_count filed is equal to the number of elements in the list of photo filed.
        self.assertEqual(media_count, photo_number)

    @allure.testcase('AO enhancer call test')
    @parameterized.expand(sources)
    @pytest.mark.critical
    def test_agent_office_call(self, source):
        wait = WebDriverWait(self.driver, 20, poll_frequency=0.5, ignored_exceptions=(Exception,))
        wait.until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
        SLPMain(self.driver).mls_btn_click()
        SLPMain(self.driver).ld_btn_click()
        DashBoard(self.driver).set_kw_source_id(source)
        DashBoard(self.driver).click_submit_btn()
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(SUBMIT_BTN))
        DashBoard(self.driver).click_view_data_btn()
        RawData(self.driver).click_raw_data_tub()
        agent = RawData(self.driver).get_list_agent_office('list_agent_mls_id')
        office = RawData(self.driver).get_list_agent_office('list_office_mls_id')
        mls_agent = agent[1:-1]
        mls_office = office[1:-1]
        expected = DBHandler.db_handler(source, mls_agent, mls_office)
        self.assertTrue(expected)

