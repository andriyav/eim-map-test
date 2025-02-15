import re
import os
import allure
import pytest
from parameterized import parameterized
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from SLP.ui.PageObjects.DashBoard.dash_board import DashBoard, SUBMIT_BTN
from SLP.ui.PageObjects.RawData.raw_data import RawData
from SLP.ui.PageObjects.SLPMain.listing_component import ListComponent
from SLP.ui.PageObjects.SLPMain.madia_component import MediaComponent
from SLP.ui.PageObjects.SLPMain.slp_main import SLPMain
from SLP.ui.PageObjects.SLPMain.source_select_component import SourceSelectComponent, SOURCE_ID
from data.mls_id_data import mls_id_dict
from data.test_data import sources
from tests.test_runner import BaseTestRunner
from selenium.webdriver.support import expected_conditions as EC
from utils.print_assertions import PrintAssertions


COUNTRY_US = "list_address.properties.country\n+\n[add]\n[add]\n[add]\n[add]\nSetConstant(const=US,const_type=str)"
COUNTRY_CA = "list_address.properties.country\n+\n[add]\n[add]\n[add]\n[add]\nSetConstant(const=CA,const_type=str)"
CO_OFFICE_PHONE = "co_list_agent_office.properties.co_list_agent_office_phone\n+\n[add]\nFirstValueProvider(json_path=[\"agent_office_phone\",\"office_phone\"],skip_values=[])\n[add]\n[add]\n[add]"
CO_PREFERRED_PHONE_SKIP = "co_list_agent_office.properties.co_list_agent_preferred_phone\n+\n[add]\nFirstValueProvider(json_path=[\"agent_mobile_phone\",\"agent_home_phone\"])\n[add]\n[add]\n[add]"
CO_PREFERRED_PHONE = "co_list_agent_office.properties.co_list_agent_preferred_phone\n+\n[add]\nFirstValueProvider(json_path=[\"agent_mobile_phone\",\"agent_home_phone\"],skip_values=[])\n[add]\n[add]\n[add]"
OFFICE_PHONE_SKIP = "list_agent_office.properties.list_agent_office_phone\n+\n[add]\nFirstValueProvider(json_path=[\"agent_office_phone\",\"office_phone\"])\n[add]\n[add]\n[add]"
OFFICE_PHONE = "list_agent_office.properties.list_agent_office_phone\n+\n[add]\nFirstValueProvider(json_path=[\"agent_office_phone\",\"office_phone\"],skip_values=[])\n[add]\n[add]\n[add]"
PREFERRED_PHONE = "list_agent_office.properties.list_agent_preferred_phone\n+\n[add]\nFirstValueProvider(json_path=[\"agent_mobile_phone\",\"agent_home_phone\"],skip_values=[])\n[add]\n[add]\n[add]"
PREFERRED_PHONE_SKIP = "list_agent_office.properties.list_agent_preferred_phone\n+\n[add]\nFirstValueProvider(json_path=[\"agent_mobile_phone\",\"agent_home_phone\"])\n[add]\n[add]\n[add]"
UNIT_NUMBER = 'list_address.properties.unit_number\n+\n[add]\n[add]\n[add]\n[add]'
STREET_SUFFIX = 'list_address.properties.street_suffix\n+\n[add]\n[add]\n[add]\n[add]'
YEAR_BUILT = 'year_built\n+\n[add]\n[add]\n[add]\n[add]'
CO_OFFICE_PHONE_SKIP = 'co_list_agent_office.properties.co_list_agent_office_phone\n+\n[add]\nFirstValueProvider(json_path=[\"agent_office_phone\",\"office_phone\"])\n[add]\n[add]\n[add]'
LIST_FIELDS = ['list_address-properties-address', 'list_address-properties-state_prov',
               'list_address-properties-postal_code', 'list_address-properties-street_name',
               'list_address-properties-street_number', 'list_address-properties-unit_number',
               'list_address-properties-street_suffix', 'list_address-properties-street_post_dir',
               'list_address-properties-street_direction']
NOT_NULLIFIED_FIELDS = ['close_price', 'current_list_price', 'hoa-items-properties-assoc_fee',
                        'hoa-items-properties-assoc_fee_search', 'marketing_info-properties-display_list_price',
                        'raw-properties-parking_total', 'structure-properties-parking_total',
                        'taxes-items-properties-tax_amt']
SCHOOL_ITEMS_EXPECTED = 'location.properties.schools.items\n+\n[add]\n[add]\n[add]\n[add]'


class TestPromotionChecklist(BaseTestRunner):

    # @allure.testcase('No elements of list_address are nullified or set constant (except country)')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_list_address_nullifier_const(self, source):
    #     title = 'No elements of list_address are nullified or set constant (except country)'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     screenshot_path = os.path.join(os.getcwd(), 'artifacts/screenshots', f'{self.id()}.png')
    #     os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    #     self.driver.save_screenshot(screenshot_path)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         slp_main.metadata_main_select(metadata)
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         actual = []
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.impl_wait_metadata()
    #                 for address_field in LIST_FIELDS:
    #                     list_fields_txt = address_field.replace('-', '.')
    #                     field = ListComponent(self.driver).get_txt_get_field(address_field)
    #                     field_actual = False
    #                     expected_field = ListComponent(self.driver).get_expected_field(list_fields_txt)
    #                     if (
    #                             'nullifier' not in field.lower() and
    #                             'skip_values=[]' in field.lower() and
    #                             'setconstant' not in field.lower()
    #                     ) or field == expected_field:
    #                         field_actual = True
    #                         actual.append(field_actual)
    #                     else:
    #                         actual.append(field_actual)
    #                         print(f'{address_field} = ', field_actual, flush=True)
    #
    #                 result = dict(zip(LIST_FIELDS, actual))
    #                 # Assert inside the try block
    #                 self.assertTrue(all(actual), result)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('list_address.country is SetConstant to country code (US or CA)')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_list_address_properties_country(self, source):
    #     title = 'list_address.country is SetConstant to country code (US or CA)'
    #     PrintAssertions.title_print(title, source)
    #     self.driver.implicitly_wait(20)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 ListComponent(self.driver).get_list_address_country()
    #                 country_code = ListComponent(self.driver).get_txt_list_address_country()
    #                 actual = False
    #                 if country_code == COUNTRY_US or country_code == COUNTRY_CA:
    #                     actual = True
    #                 self.assertTrue(actual, country_code)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase(
    #     'co_list_agent_office_phone are mapped with FirstValueProvider:("agent_office_phone","office_phone")')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_co_list_agent_office_phone(self, source):
    #     title = 'co_list_agent_office_phone are mapped with FirstValueProvider:("agent_office_phone","office_phone")'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 ListComponent(self.driver).get_co_list_agent_office_phone()
    #                 actual = ListComponent(self.driver).get_txt_co_list_agent_office_phone()
    #                 result = False
    #                 if actual == CO_OFFICE_PHONE or actual == CO_OFFICE_PHONE_SKIP:
    #                     result = True
    #                 self.assertTrue(result)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('co_list_agent_preferred_phone are mapped with FirstValueProvider:("agent_mobile_phone","agent_home_phone"')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_co_list_agent_preferred_phone(self, source):
    #     title = 'co_list_agent_preferred_phone are mapped with FirstValueProvider:("agent_mobile_phone","agent_home_phone"'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 ListComponent(self.driver).get_co_list_agent_preferred_phone()
    #                 actual = ListComponent(self.driver).get_txt_co_list_agent_preferred_phone()
    #                 result = False
    #                 if actual == CO_PREFERRED_PHONE or actual == CO_PREFERRED_PHONE_SKIP:
    #                     result = True
    #                 self.assertTrue(result)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('list_agent_office_phone are mapped with FirstValueProvider:("agent_office_phone","office_phone")"')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_list_agent_office_phone(self, source):
    #     title = 'list_agent_office_phone are mapped with FirstValueProvider:("agent_office_phone","office_phone")"'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 ListComponent(self.driver).get_list_agent_office_phone()
    #                 actual = ListComponent(self.driver).get_txt_list_agent_office_phone()
    #                 result = False
    #                 if actual == OFFICE_PHONE or actual == OFFICE_PHONE_SKIP:
    #                     result = True
    #                 self.assertTrue(result)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('list_agent_preferred_phone are mapped with FirstValueProvider:("agent_mobile_phone","agent_home_phone")')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_list_agent_preferred_phone(self, source):
    #     title = 'list_agent_preferred_phone are mapped with FirstValueProvider:("agent_mobile_phone","agent_home_phone")'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 ListComponent(self.driver).get_list_agent_preferred_phone()
    #                 actual = ListComponent(self.driver).get_txt_list_agent_preferred_phone()
    #                 result = False
    #                 if actual == PREFERRED_PHONE or actual == PREFERRED_PHONE_SKIP:
    #                     result = True
    #                 self.assertTrue(result)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('Validate mls_source_id and sa_source_id are correct from here (NOT kw_id)')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_mls_id_sa_id(self, source):
    #     title = 'Validate mls_source_id and sa_source_id are correct from here (NOT kw_id)'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 ListComponent(self.driver).get_list_sa_id()
    #                 sa_id = ListComponent(self.driver).get_txt_ist_sa_id()
    #                 mls_id = ListComponent(self.driver).get_txt_list_mls_id()
    #                 actual = [mls_id, sa_id]
    #                 target_list = mls_id_dict.get(source)
    #                 mls_id_target = f'mls_id\n+\n[add]\n[add]\n[add]\n[add]\nSetConstant(const={target_list[0]},const_type=str)'
    #                 sa_id_target = f'sa_source_id\n+\n[add]\n[add]\n[add]\n[add]\nSetConstant(const={target_list[1]},const_type=int)'
    #                 target = [mls_id_target, sa_id_target]
    #                 self.assertEqual(actual, target, sa_id)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('Validate mls_id is the correct value')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_dashboard_source_number(self, source):
    #     title = 'Validate mls_id is the correct value'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     dash_board = DashBoard(self.driver)
    #     slp_main.source_select(source)
    #     SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
    #     slp_main.mls_btn_click()
    #     slp_main.ld_btn_click()
    #     dash_board.set_kw_source_id(source)
    #     dash_board.click_submit_btn()
    #     actual = DashBoard(self.driver).get_source_id_txt()
    #     try:
    #         self.assertEqual(actual, source)
    #         PrintAssertions.ok_print(class_txt='Property')
    #     except:
    #         PrintAssertions.nok_print(class_txt='Property')
    #
    # @allure.testcase('Currency_code must be UPPER')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_currency_code(self, source):
    #     title = 'Currency_code must be UPPER'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 field = ListComponent(self.driver).get_txt_get_field('currency_code')
    #                 match = re.search(r"const=([A-Za-z]{3})", field)
    #                 if match:
    #                     currency_code = match.group(1)
    #                     is_upper = currency_code.isupper()
    #                 self.assertTrue(is_upper, field)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('list_dt is mapped')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_list_dt(self, source):
    #     title = 'list_dt is mapped'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 field = ListComponent(self.driver).get_txt_get_field('list_dt')
    #                 field_actual = False
    #                 if 'json_path=' in field:
    #                     field_actual = True
    #                 self.assertTrue(field_actual, field)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('raw.properties.list_status is mapped')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_raw_properties_list_status(self, source):
    #     title = 'raw.properties.list_status is mapped'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 field = ListComponent(self.driver).get_txt_get_field('raw-properties-list_status')
    #                 field_actual = False
    #                 if 'json_path=' in field:
    #                     field_actual = True
    #                 self.assertTrue(field_actual, field)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('Kww_region has no mapping')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_kww_region(self, source):
    #     title = 'Kww_region has no mapping'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 SLPMain(self.driver).impl_wait_metadata()
    #                 expected_field = ListComponent(self.driver).get_expected_field('kww_region')
    #                 actual_field = ListComponent(self.driver).get_txt_get_field('kww_region')
    #                 self.assertEqual(actual_field, expected_field, actual_field)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('Price_history must use PriceHistoryEnhancer with ListPrice input')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_price_history(self, source):
    #     title = 'Price_history must use PriceHistoryEnhancer with ListPrice input'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         actual = []
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 field_actual = False
    #                 price_history = ListComponent(self.driver).get_txt_get_field('price_history')
    #                 if 'json_path=' in price_history and 'PriceHistoryEnhancer' in price_history:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history = ', field_actual, flush=True)
    #
    #                 price_history_items = ListComponent(self.driver).get_txt_get_field('price_history-items')
    #                 field_actual = False
    #                 if 'ValueProvider(json_path=[],skip_values=[])' in price_history_items:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history-items = ', field_actual, flush=True)
    #
    #                 price_history_in_use = ListComponent(self.driver).get_txt_get_field(
    #                     'price_history-items-properties-in_use')
    #                 field_actual = False
    #                 if 'ValueProvider(json_path=in_use,skip_values=[])' in price_history_in_use:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history-items-properties-in_use = ', field_actual, flush=True)
    #
    #                 price_history_percent_change = ListComponent(self.driver).get_txt_get_field(
    #                     'price_history-items-properties-percent_change')
    #                 field_actual = False
    #                 if 'ValueProvider(json_path=percent_change,skip_values=[])' in price_history_percent_change:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history.items.properties.percent_change = ', field_actual, flush=True)
    #
    #                 price_history_update_at = ListComponent(self.driver).get_txt_get_field(
    #                     'price_history-items-properties-price_updated_at')
    #                 field_actual = False
    #                 if 'ValueProvider(json_path=price_updated_at,skip_values=[])' in price_history_update_at:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history.items.properties.price_updated_at = ', field_actual, flush=True)
    #
    #                 price_history_current_list_price = ListComponent(self.driver).get_txt_get_field(
    #                     'price_history-items-properties-current_list_price')
    #                 field_actual = False
    #                 if 'ValueProvider(json_path=current_list_price,skip_values=[])' in price_history_current_list_price:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history.items.properties.current_list_price = ', field_actual, flush=True)
    #
    #                 price_history_previous_list_price = ListComponent(self.driver).get_txt_get_field(
    #                     'price_history-items-properties-previous_list_price')
    #                 field_actual = False
    #                 if 'ValueProvider(json_path=previous_list_price,skip_values=[])' in price_history_previous_list_price:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history.items.properties.previous_list_price = ', field_actual, flush=True)
    #                 self.assertTrue(all(actual))
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('list_address.state_prov returns 2-letter State code')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_state_prov(self, source):
    #     title = 'list_address.state_prov returns 2-letter State code'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     dash_board = DashBoard(self.driver)
    #     slp_main.source_select(source)
    #     SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
    #     slp_main.mls_btn_click()
    #     slp_main.ld_btn_click()
    #     dash_board.set_kw_source_id(source)
    #     dash_board.click_submit_btn()
    #     WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable(SUBMIT_BTN))
    #     dash_board.click_view_data_btn()
    #     RawData(self.driver).click_raw_data_tub()
    #     actual_raw = RawData(self.driver).get_list_address('state_prov')
    #     actual = actual_raw.replace('"', '')
    #     result = False
    #     if len(actual) == 2:
    #         result = True
    #         try:
    #             self.assertTrue(result, actual)
    #             PrintAssertions.ok_print(class_txt='property')
    #         except:
    #             PrintAssertions.nok_print(class_txt='property')
    #
    # @allure.testcase('All available elements of list_address.properties.address are included')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_list_address(self, source):
    #     title = 'All available elements of list_address.properties.address are included'
    #     PrintAssertions.title_print(title, source)
    #     self.driver.implicitly_wait(20)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 actual = ListComponent(self.driver).get_txt_get_field('list_address-properties-address')
    #                 result = False
    #                 if 'a_street_number' in actual and 'b_street_dir_prefix' in actual \
    #                         and 'c_street_name' in actual and 'd_street_suffix' in actual \
    #                         and 'e_street_dir_suffix' in actual and 'f_unit_number' in actual \
    #                         and 'g_city' in actual and 'h_state_or_province' in actual \
    #                         and 'i_postal_code' in actual:
    #                     result = True
    #                 self.assertTrue(result, actual)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('List_address.coordinates should utilize Latitude and Longitude')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_list_address_coordinates(self, source):
    #     title = 'List_address.coordinates should utilize Latitude and Longitude'
    #     PrintAssertions.title_print(title, source)
    #     self.driver.implicitly_wait(20)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 actual_gp = ListComponent(self.driver).get_txt_get_field('list_address-properties-coordinates_gp')
    #                 actual_gs = ListComponent(self.driver).get_txt_get_field('list_address-properties-coordinates_gs')
    #                 result = False
    #                 if 'source_lat' in actual_gp and 'source_lon' in actual_gp and 'CoordinatesEnhancer' in actual_gp \
    #                         and 'source_lat' in actual_gs and 'source_lon' in actual_gs and 'CoordinatesEnhancer' in actual_gs:
    #                     result = True
    #                 self.assertTrue(result, f'{actual_gs}, ,{actual_gp}')
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    #
    # @allure.testcase('Field year_built uses the rule ValidateYearBuilt')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_year_built(self, source):
    #     title = 'Field year_built uses the rule ValidateYearBuilt'
    #     PrintAssertions.title_print(title, source)
    #     self.driver.implicitly_wait(20)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 actual = ListComponent(self.driver).get_txt_get_field('year_built')
    #                 result = False
    #                 if actual == YEAR_BUILT or 'ValidateYearBuilt' in actual:
    #                     result = True
    #                 self.assertTrue(result, actual)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('Do NOT Nullify any of these fields')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_not_nullify(self, source):
    #     title = 'Do NOT Nullify any of these fields'
    #     PrintAssertions.title_print(title, source)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     screenshot_path = os.path.join(os.getcwd(), 'artifacts/screenshots', f'{self.id()}.png')
    #     os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
    #     self.driver.save_screenshot(screenshot_path)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         slp_main.metadata_main_select(metadata)
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         actual = []
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.impl_wait_metadata()
    #                 for address_field in NOT_NULLIFIED_FIELDS:
    #                     list_fields_txt = address_field.replace('-', '.')
    #                     field = ListComponent(self.driver).get_txt_get_field(address_field)
    #                     field_actual = False
    #                     expected_field = ListComponent(self.driver).get_expected_field(list_fields_txt)
    #                     if (
    #                             'nullifier' not in field.lower() and
    #                             'skip_values=[]' in field.lower()
    #                     ) or field == expected_field:
    #                         field_actual = True
    #                         actual.append(field_actual)
    #                     else:
    #                         actual.append(field_actual)
    #                         print(f'{address_field} = ', field_actual, flush=True)
    #                 result = dict(zip(NOT_NULLIFIED_FIELDS, actual))
    #                 # Assert inside the try block
    #                 self.assertTrue(all(actual), result)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)
    #
    # @allure.testcase('schools.items does NOT need the empty bracket Value Provider')
    # @parameterized.expand(sources)
    # @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    # def test_schools_items(self, source):
    #     title = 'schools.items does NOT need the empty bracket Value Provider'
    #     PrintAssertions.title_print(title, source)
    #     self.driver.implicitly_wait(20)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     slp_main = SLPMain(self.driver)
    #     slp_main.source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 slp_main.metadata_main_select(metadata)
    #                 slp_main.impl_wait_metadata()
    #                 ListComponent(self.driver).get_list_address_country()
    #                 actual = ListComponent(self.driver).get_txt_get_field('location-properties-schools-items')
    #                 self.assertEqual(actual, SCHOOL_ITEMS_EXPECTED)
    #                 PrintAssertions.ok_print(class_txt)
    #             except AssertionError as e:
    #                 # Handle assertion errors separately
    #                 PrintAssertions.nok_print(class_txt)
    #                 raise e  # Re-raise to ensure the test fails
    #             except NoSuchElementException as e:
    #                 PrintAssertions.no_map_print(class_txt)

    @allure.testcase('Ph_category is mapped with the rule "PhotoCategory" applied')
    @parameterized.expand(sources)
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_list_address_properties_country(self, source):
        title = 'Ph_category is mapped with the rule "PhotoCategory" applied'
        PrintAssertions.title_print(title, source)
        self.driver.implicitly_wait(20)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
        slp_main = SLPMain(self.driver)
        media = MediaComponent(self.driver)
        slp_main.source_select(source)
        slp_main.select_photo_tub()
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
            with self.subTest(metadata=class_txt):
                try:
                    slp_main.metadata_main_select(metadata)
                    slp_main.impl_wait_media_metadata()
                    ph_text = media.get_txt_ph_type()
                    result = False
                    if 'PhotoCategory' in ph_text:
                        result = True
                    self.assertTrue(result, ph_text)
                    PrintAssertions.ok_print(class_txt)
                except AssertionError as e:
                    # Handle assertion errors separately
                    PrintAssertions.nok_print(class_txt)
                    raise e  # Re-raise to ensure the test fails
                except NoSuchElementException as e:
                    PrintAssertions.no_map_print(class_txt)