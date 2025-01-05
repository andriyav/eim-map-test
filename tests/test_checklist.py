import re
import os

import allure
import pytest
from parameterized import parameterized
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from SLP.ui.PageObjects.DashBoard.dash_board import DashBoard
from SLP.ui.PageObjects.SLPMain.listing_component import ListComponent
from SLP.ui.PageObjects.SLPMain.slp_main import SLPMain
from SLP.ui.PageObjects.SLPMain.source_select_component import SourceSelectComponent
from data.mls_id_data import mls_id_dict
from data.test_data import sources
from tests.test_runner import BaseTestRunner
from selenium.webdriver.support import expected_conditions as EC

SOURCE_ID = (By.CSS_SELECTOR,' #sources')
COUNTRY_US = "list_address.properties.country\n+\n[add]\n[add]\n[add]\n[add]\nSetConstant(const=US,const_type=str)"
COUNTRY_CA = "list_address.properties.country\n+\n[add]\n[add]\n[add]\n[add]\nSetConstant(const=CA,const_type=str)"
CO_OFFICE_PHONE = "co_list_agent_office.properties.co_list_agent_office_phone\n+\n[add]\nFirstValueProvider(json_path=[\"agent_office_phone\",\"office_phone\"],skip_values=[])\n[add]\n[add]\n[add]"
CO_PREFERRED_PHONE = "co_list_agent_office.properties.co_list_agent_preferred_phone\n+\n[add]\nFirstValueProvider(json_path=[\"agent_mobile_phone\",\"agent_home_phone\"],skip_values=[])\n[add]\n[add]\n[add]"
OFFICE_PHONE = "list_agent_office.properties.list_agent_office_phone\n+\n[add]\nFirstValueProvider(json_path=[\"agent_office_phone\",\"office_phone\"],skip_values=[])\n[add]\n[add]\n[add]"
PREFERRED_PHONE = "list_agent_office.properties.list_agent_preferred_phone\n+\n[add]\nFirstValueProvider(json_path=[\"agent_mobile_phone\",\"agent_home_phone\"],skip_values=[])\n[add]\n[add]\n[add]"
UNIT_NUMBER = """list_address.properties.unit_number
+
[add]
[add]
[add]
[add]"""

STREET_SUFFIX = """list_address.properties.street_suffix
+
[add]
[add]
[add]
[add]"""

LIST_FIELDS = ['list_address-properties-address', 'list_address-properties-state_prov',
               'list_address-properties-postal_code', 'list_address-properties-street_name',
               'list_address-properties-street_number', 'list_address-properties-unit_number',
               'list_address-properties-street_suffix', 'list_address-properties-street_post_dir',
               'list_address-properties-street_direction']



class TestPromotionChecklist(BaseTestRunner):

    @allure.testcase('No elements of list_address are nullified or set constant (except country)')
    @parameterized.expand(sources)
    @pytest.mark.filterwarnings("ignore::DeprecationWarning")
    def test_list_address_nullifier_const(self, source):
        '''No elements of list_address are nullified or set constant (except country)'''
        print("No elements of list_address are nullified or set constant (except country)", flush=True)
        print(f"kw_id = {source}", flush=True)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        screenshot_path = os.path.join(os.getcwd(), 'artifacts/screenshots', f'{self.id()}.png')
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        self.driver.save_screenshot(screenshot_path)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            SLPMain(self.driver).metadata_main_select(metadata)
            class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
            actual = []
            with self.subTest(metadata=class_txt):
                try:
                    SLPMain(self.driver).impl_wait_metadata()
                    for address_field in LIST_FIELDS:
                        list_fields_txt = address_field.replace('-', '.')
                        field = ListComponent(self.driver).get_txt_get_field(address_field)
                        field_actual = False
                        expected_field = ListComponent(self.driver).get_expected_field(list_fields_txt)
                        if (
                                'nullifier' not in field.lower() and
                                'skip_values=[]' in field.lower() and
                                'setconstant' not in field.lower()
                        ) or field == expected_field:
                            field_actual = True
                            actual.append(field_actual)
                        else:
                            actual.append(field_actual)
                            print(f'{address_field} = ', field_actual)

                    result = dict(zip(LIST_FIELDS, actual))

                    # Assert inside the try block
                    self.assertTrue(all(actual), result)
                    with allure.step(f"Metadata = {class_txt} Ok ✅"):
                        print(f'Metadata = {class_txt} Ok ✅', flush=True)

                except AssertionError as e:
                    # Handle assertion errors separately
                    with allure.step(f"Metadata = {class_txt} Failed ❌"):
                        print(f'\nMetadata = {class_txt} Failed ❌', flush=True)
                    raise e  # Re-raise to ensure the test fails

                except NoSuchElementException as e:
                    with allure.step(f"Looks like the class {class_txt} is not mapped"):
                        print(f"Looks like the class {class_txt} is not mapped", flush=True)

    # @allure.testcase('list_address.country is SetConstant to country code (US or CA)')
    # @parameterized.expand(sources)
    # def test_list_address_properties_country(self, source):
    #     '''list_address.country is SetConstant to country code (US or CA)'''
    #     print("list_address.country is SetConstant to country code (US or CA)", flush=True)
    #     print(f"kw_id = {source}", flush=True)
    #     self.driver.implicitly_wait(20)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     SLPMain(self.driver).source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 SLPMain(self.driver).metadata_main_select(metadata)
    #                 SLPMain(self.driver).impl_wait_metadata()
    #                 ListComponent(self.driver).get_list_address_country()
    #                 country_code = ListComponent(self.driver).get_txt_list_address_country()
    #                 actual = False
    #                 if country_code == COUNTRY_US or country_code == COUNTRY_CA:
    #                     actual = True
    #                 try:
    #                     self.assertTrue(actual)
    #                     print(f'Metadata = {class_txt} Ok ✅', flush=True)
    #                 except:
    #                     print(f'Metadata = {class_txt} Failed ❌ in {country_code}', flush=True)
    #                     self.assertTrue(actual)
    #             except NoSuchElementException as e:
    #                 print(f"looks like the class {class_txt} is not mapped")
    #     print("----------------------------------------------------------------------", flush=True)

    # @allure.testcase('''co_list_agent_office_phone are mapped with FirstValueProvider:('agent_office_phone","office_phone")''')
    # @parameterized.expand(sources)
    # def test_co_list_agent_office_phone(self, source):
    #     ''' co_list_agent_office_phone are mapped with
    #         FirstValueProvider:("agent_office_phone","office_phone")" '''
    #     print(
    #         '''co_list_agent_office_phone are mapped with FirstValueProvider:('agent_office_phone","office_phone")"''',
    #         flush=True)
    #     print(f"kw_id = {source}", flush=True)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     SLPMain(self.driver).source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 SLPMain(self.driver).metadata_main_select(metadata)
    #                 SLPMain(self.driver).impl_wait_metadata()
    #                 ListComponent(self.driver).get_co_list_agent_office_phone()
    #                 actual = ListComponent(self.driver).get_txt_co_list_agent_office_phone()
    #                 try:
    #                     self.assertEqual(CO_OFFICE_PHONE, actual)
    #                     print(f'Metadata = {class_txt} Ok ✅', flush=True)
    #                 except:
    #                     print(f'Metadata = {class_txt} Failed ❌ in {actual}', flush=True)
    #                     self.assertEqual(CO_OFFICE_PHONE, actual)
    #             except NoSuchElementException as e:
    #                 print(f"looks like the class {class_txt} is not mapped", flush=True)
    #
    #     print("----------------------------------------------------------------------", flush=True)
    #
    # @allure.testcase('4')
    # @parameterized.expand(sources)
    # def test_co_list_agent_preferred_phone(self, source):
    #     '''co_list_agent_preferred_phone are mapped with
    #     FirstValueProvider:("agent_mobile_phone","agent_home_phone"'''
    #     print(
    #         '''co_list_agent_preferred_phone are mapped with FirstValueProvider:("agent_mobile_phone","agent_home_phone)"''',
    #         flush=True)
    #     print(f"kw_id = {source}", flush=True)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     SLPMain(self.driver).source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 SLPMain(self.driver).metadata_main_select(metadata)
    #                 SLPMain(self.driver).impl_wait_metadata()
    #                 ListComponent(self.driver).get_co_list_agent_preferred_phone()
    #                 actual = ListComponent(self.driver).get_txt_co_list_agent_preferred_phone()
    #                 try:
    #                     self.assertEqual(CO_PREFERRED_PHONE, actual)
    #                     print(f'Metadata = {class_txt} Ok ✅', flush=True)
    #                 except:
    #                     print(f'Metadata = {class_txt} Failed ❌ in {actual}', flush=True)
    #                     self.assertEqual(CO_PREFERRED_PHONE, actual)
    #             except NoSuchElementException as e:
    #                 print(f"looks like the class {class_txt} is not mapped", flush=True)
    #     print("----------------------------------------------------------------------", flush=True)
    #
    # @allure.testcase('5')
    # @parameterized.expand(sources)
    # def test_list_agent_office_phone(self, source):
    #     '''list_agent_office_phone are mapped with
    # `   FirstValueProvider:("agent_office_phone","office_phone")" '''
    #     print('''list_agent_office_phone are mapped with FirstValueProvider:("agent_office_phone","office_phone")" ''',
    #           flush=True)
    #     print(f"kw_id = {source}", flush=True)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     SLPMain(self.driver).source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 SLPMain(self.driver).metadata_main_select(metadata)
    #                 SLPMain(self.driver).impl_wait_metadata()
    #                 ListComponent(self.driver).get_list_agent_office_phone()
    #                 actual = ListComponent(self.driver).get_txt_list_agent_office_phone()
    #                 try:
    #                     self.assertEqual(OFFICE_PHONE, actual)
    #                     print(f'Metadata = {class_txt} Ok ✅', flush=True)
    #                 except:
    #                     print(f'Metadata = {class_txt} Failed ❌ in {actual}', flush=True)
    #                     self.assertEqual(OFFICE_PHONE, actual)
    #             except NoSuchElementException as e:
    #                 print(f"looks like the class {class_txt} is not mapped", flush=True)
    #     print("----------------------------------------------------------------------", flush=True)
    #
    # @allure.testcase('6')
    # @parameterized.expand(sources)
    # def test_list_agent_preferred_phone(self, source):
    #     ''' list_agent_preferred_phone are mapped with FirstValueProvider:("agent_mobile_phone","agent_home_phone")'''
    #     print(
    #         ''' list_agent_preferred_phone are mapped with FirstValueProvider:("agent_mobile_phone","agent_home_phone")''',
    #         flush=True)
    #     print(f"kw_id = {source}", flush=True)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     SLPMain(self.driver).source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 SLPMain(self.driver).metadata_main_select(metadata)
    #                 SLPMain(self.driver).impl_wait_metadata()
    #                 ListComponent(self.driver).get_list_agent_preferred_phone()
    #                 actual = ListComponent(self.driver).get_txt_list_agent_preferred_phone()
    #                 try:
    #                     self.assertEqual(PREFERRED_PHONE, actual)
    #                     print(f'Metadata = {class_txt} Ok ✅', flush=True)
    #                 except:
    #                     print(f'Metadata = {class_txt} Failed ❌ in {actual}', flush=True)
    #                     self.assertEqual(PREFERRED_PHONE, actual)
    #             except NoSuchElementException as e:
    #                 print(f"looks like the class {class_txt} is not mapped", flush=True)
    #     print("----------------------------------------------------------------------", flush=True)
    #
    # @allure.testcase('7')
    # @parameterized.expand(sources)
    # def test_mls_id_sa_id(self, source):
    #     '''Validate mls_source_id and sa_source_id are correct from here (NOT kw_id)'''
    #     print('''Validate mls_source_id and sa_source_id are correct from here (NOT kw_id)''', flush=True)
    #     print(f"kw_id = {source}", flush=True)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     SLPMain(self.driver).source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 SLPMain(self.driver).metadata_main_select(metadata)
    #                 SLPMain(self.driver).impl_wait_metadata()
    #                 ListComponent(self.driver).get_list_sa_id()
    #                 sa_id = ListComponent(self.driver).get_txt_ist_sa_id()
    #                 mls_id = ListComponent(self.driver).get_txt_list_mls_id()
    #                 actual = [mls_id, sa_id]
    #                 target_list = mls_id_dict.get(source)
    #                 mls_id_target = f'mls_id\n+\n[add]\n[add]\n[add]\n[add]\nSetConstant(const={target_list[0]},const_type=str)'
    #                 sa_id_target = f'sa_source_id\n+\n[add]\n[add]\n[add]\n[add]\nSetConstant(const={target_list[1]},const_type=int)'
    #                 target = [mls_id_target, sa_id_target]
    #                 try:
    #                     self.assertEqual(actual, target)
    #                     print(f'Metadata = {class_txt} Ok ✅', flush=True)
    #                 except:
    #                     print(f'Metadata = {class_txt} Failed ❌ in {actual}', flush=True)
    #                     self.assertEqual(actual, target)
    #             except NoSuchElementException as e:
    #                 print(f"looks like the class {class_txt} is not mapped", flush=True)
    #     print("----------------------------------------------------------------------", flush=True)
    #
    # @allure.testcase('8')
    # @parameterized.expand(sources)
    # def test_dashboard_source_number(self, source):
    #     '''Validate mls_id is the correct value'''
    #     print('''Validate mls_id is the correct value from here''', flush=True)
    #     print(f"kw_id = {source}", flush=True)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     SLPMain(self.driver).source_select(source)
    #     SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
    #     SLPMain(self.driver).mls_btn_click()
    #     SLPMain(self.driver).ld_btn_click()
    #     DashBoard(self.driver).set_kw_source_id(source)
    #     DashBoard(self.driver).click_submit_btn()
    #     actual = DashBoard(self.driver).get_source_id_txt()
    #     try:
    #         self.assertEqual(actual, source)
    #         print(f' Ok ✅', flush=True)
    #     except:
    #         print(f'Failed ❌ in {actual}', flush=True)
    #         self.assertEqual(actual, source)
    #     print("----------------------------------------------------------------------", flush=True)
    #
    # @allure.testcase('9')
    # @parameterized.expand(sources)
    # def test_currency_code(self, source):
    #     '''Currency_code must be UPPER'''
    #     print('''Currency_code must be UPPER''', flush=True)
    #     print(f"kw_id = {source}", flush=True)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     SLPMain(self.driver).source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 SLPMain(self.driver).metadata_main_select(metadata)
    #                 SLPMain(self.driver).impl_wait_metadata()
    #                 field = ListComponent(self.driver).get_txt_get_field('currency_code')
    #                 match = re.search(r"const=([A-Za-z]{3})", field)
    #                 if match:
    #                     currency_code = match.group(1)
    #                     is_upper = currency_code.isupper()
    #                 try:
    #                     self.assertTrue(is_upper)
    #                     print(f'Metadata = {class_txt} Ok ✅', flush=True)
    #                 except:
    #                     print(f'Metadata = {class_txt} Failed ❌ in {field}', flush=True)
    #                     self.assertTrue(is_upper)
    #             except NoSuchElementException as e:
    #                 print(f"looks like the class {class_txt} is not mapped", flush=True)
    #
    #     print("----------------------------------------------------------------------", flush=True)
    #
    # @allure.testcase('10')
    # @parameterized.expand(sources)
    # def test_list_dt(self, source):
    #     '''list_dt is mapped'''
    #     print('''list_dt is mapped''', flush=True)
    #     print(f"kw_id = {source}", flush=True)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     SLPMain(self.driver).source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 SLPMain(self.driver).metadata_main_select(metadata)
    #                 SLPMain(self.driver).impl_wait_metadata()
    #                 field = ListComponent(self.driver).get_txt_get_field('list_dt')
    #                 field_actual = False
    #                 if 'json_path=' in field:
    #                     field_actual = True
    #                 try:
    #                     self.assertTrue(field_actual)
    #                     print(f'Metadata = {class_txt} Ok ✅', flush=True)
    #                 except:
    #                     print(f'Metadata = {class_txt} Failed ❌ in {field}', flush=True)
    #                     self.assertTrue(field_actual)
    #             except NoSuchElementException as e:
    #                 print(f"looks like the class {class_txt} is not mapped", flush=True)
    #     print("----------------------------------------------------------------------", flush=True)
    #
    # @allure.testcase('11')
    # @parameterized.expand(sources)
    # def test_raw_properties_list_status(self, source):
    #     '''raw.properties.list_status is mapped'''
    #     print('''raw.properties.list_status is mapped''', flush=True)
    #     print(f"kw_id = {source}", flush=True)
    #     WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
    #     SLPMain(self.driver).source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 SLPMain(self.driver).metadata_main_select(metadata)
    #                 SLPMain(self.driver).impl_wait_metadata()
    #                 field = ListComponent(self.driver).get_txt_get_field('raw-properties-list_status')
    #                 field_actual = False
    #                 if 'json_path=' in field:
    #                     field_actual = True
    #                 try:
    #                     self.assertTrue(field_actual)
    #                     print(f'Metadata = {class_txt} Ok ✅', flush=True)
    #                 except:
    #                     print(f'Metadata = {class_txt} Failed ❌ in {field}', flush=True)
    #                     self.assertTrue(field_actual)
    #             except NoSuchElementException as e:
    #                 print(f"looks like the class {class_txt} is not mapped", flush=True)
    #     print("----------------------------------------------------------------------", flush=True)
    #
    # @allure.testcase('12')
    # @parameterized.expand(sources)
    # def test_kww_region(self, source):
    #     ''' Kww_region has no mapping '''
    #     print(''' Kww_region has no mapping ''', flush=True)
    #     print(f"kw_id = {source}", flush=True)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     SLPMain(self.driver).source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 SLPMain(self.driver).metadata_main_select(metadata)
    #                 SLPMain(self.driver).impl_wait_metadata()
    #                 expected_field = ListComponent(self.driver).get_expected_field('kww_region')
    #                 actual_field = ListComponent(self.driver).get_txt_get_field('kww_region')
    #                 try:
    #                     self.assertEqual(actual_field, expected_field)
    #                     print(f'Metadata = {class_txt} Ok ✅', flush=True)
    #                 except:
    #                     print(f'Metadata = {class_txt} Failed ❌ in {actual_field}', flush=True)
    #                     self.assertEqual(actual_field, expected_field)
    #             except NoSuchElementException as e:
    #                 print(f"looks like the class {class_txt} is not mapped", flush=True)
    #     print("----------------------------------------------------------------------", flush=True)
    #
    # @allure.testcase('13')
    # @parameterized.expand(sources)
    # def test_price_history(self, source):
    #     ''' Price_history must use PriceHistoryEnhancer with ListPrice input'''
    #     print('''Price_history must use PriceHistoryEnhancer with ListPrice input''', flush=True)
    #     print(f"kw_id = {source}", flush=True)
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(SOURCE_ID))
    #     SLPMain(self.driver).source_select(source)
    #     metadata_numbers = ListComponent(self.driver).get_metadata_number()
    #     for metadata in range(1, metadata_numbers):
    #         class_txt = ListComponent(self.driver).get_metadata_text(metadata + 1)
    #         actual = []
    #         with self.subTest(metadata=class_txt):
    #             try:
    #                 SLPMain(self.driver).metadata_main_select(metadata)
    #                 SLPMain(self.driver).impl_wait_metadata()
    #                 field_actual = False
    #                 price_history = ListComponent(self.driver).get_txt_get_field('price_history')
    #                 if 'json_path=' in price_history and 'PriceHistoryEnhancer' in price_history:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history = ', field_actual)
    #
    #                 price_history_items = ListComponent(self.driver).get_txt_get_field('price_history-items')
    #                 field_actual = False
    #                 if 'ValueProvider(json_path=[],skip_values=[])' in price_history_items:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history-items = ', field_actual)
    #
    #                 price_history_in_use = ListComponent(self.driver).get_txt_get_field(
    #                     'price_history-items-properties-in_use')
    #                 field_actual = False
    #                 if 'ValueProvider(json_path=in_use,skip_values=[])' in price_history_in_use:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history-items-properties-in_use = ', field_actual)
    #
    #                 price_history_percent_change = ListComponent(self.driver).get_txt_get_field(
    #                     'price_history-items-properties-percent_change')
    #                 field_actual = False
    #                 if 'ValueProvider(json_path=percent_change,skip_values=[])' in price_history_percent_change:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history.items.properties.percent_change = ', field_actual)
    #
    #                 price_history_update_at = ListComponent(self.driver).get_txt_get_field(
    #                     'price_history-items-properties-price_updated_at')
    #                 field_actual = False
    #                 if 'ValueProvider(json_path=price_updated_at,skip_values=[])' in price_history_update_at:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history.items.properties.price_updated_at = ', field_actual)
    #
    #                 price_history_current_list_price = ListComponent(self.driver).get_txt_get_field(
    #                     'price_history-items-properties-current_list_price')
    #                 field_actual = False
    #                 if 'ValueProvider(json_path=current_list_price,skip_values=[])' in price_history_current_list_price:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history.items.properties.current_list_price = ', field_actual)
    #
    #                 price_history_previous_list_price = ListComponent(self.driver).get_txt_get_field(
    #                     'price_history-items-properties-previous_list_price')
    #                 field_actual = False
    #                 if 'ValueProvider(json_path=previous_list_price,skip_values=[])' in price_history_previous_list_price:
    #                     field_actual = True
    #                     actual.append(field_actual)
    #                 else:
    #                     actual.append(field_actual)
    #                     print('price_history.items.properties.previous_list_price = ', field_actual)
    #                 try:
    #                     self.assertTrue(all(actual))
    #                     print(f'Metadata = {class_txt} Ok ✅', flush=True)
    #                 except:
    #                     print(f'Metadata = {class_txt} Failed ❌ in {actual}', flush=True)
    #                     self.assertTrue(all(actual))
    #             except NoSuchElementException as e:
    #                 print(f"looks like the class {class_txt} is not mapped", flush=True)
    #     print("----------------------------------------------------------------------", flush=True)