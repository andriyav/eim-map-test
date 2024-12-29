import re

from parameterized import parameterized
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os

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

    # @parameterized.expand(sources)
    # def test_list_address_nullifier_const(self, source):
    #     pass


    @parameterized.expand(sources)
    def test_list_address_nullifier_const(self, source):
        '''No elements of list_address are nullified or set constant (except country)'''

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        screenshot_path = os.path.join(os.getcwd(), 'artifacts/screenshots', f'{self.id()}.png')
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        self.driver.save_screenshot(screenshot_path)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                actual = []
                for address_field in LIST_FIELDS:
                    list_fields_txt = address_field.replace('-', '.')
                    field = ListComponent(self.driver).get_txt_get_field(address_field)
                    field_actual = False
                    expected_field = ListComponent(self.driver).get_expected_field(list_fields_txt)
                    if ('nullifier' not in field.lower() and 'skip_values=[]' in field.lower() and 'setconstant' not in field.lower()) or field == expected_field:
                        field_actual = True
                        actual.append(field_actual)
                    else:
                        actual.append(field_actual)
                        print(f'{address_field} = ', field_actual)
                result = dict(zip(LIST_FIELDS, actual))
                self.assertTrue(all(actual), result)

    @parameterized.expand(sources)
    def test_list_address_properties_country(self, source):
        '''list_address.country is SetConstant to country code (US or CA)'''
        self.driver.implicitly_wait(20)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                ListComponent(self.driver).get_list_address_country()
                country_code = ListComponent(self.driver).get_txt_list_address_country()
                actual = False
                if country_code == COUNTRY_US or country_code == COUNTRY_CA:
                    actual = True
                self.assertTrue(actual)

    @parameterized.expand(sources)
    def test_co_list_agent_office_phone(self, source):
        ''' co_list_agent_office_phone are mapped with
FirstValueProvider:("agent_office_phone","office_phone")" '''
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                ListComponent(self.driver).get_co_list_agent_office_phone()
                actual = ListComponent(self.driver).get_txt_co_list_agent_office_phone()
                self.assertEqual(CO_OFFICE_PHONE, actual)

    @parameterized.expand(sources)
    def test_co_list_agent_preferred_phone(self, source):
        '''co_list_agent_preferred_phone are mapped with
FirstValueProvider:("agent_mobile_phone","agent_home_phone"'''
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                ListComponent(self.driver).get_co_list_agent_preferred_phone()
                actual = ListComponent(self.driver).get_txt_co_list_agent_preferred_phone()
                self.assertEqual(CO_PREFERRED_PHONE, actual)

    @parameterized.expand(sources)
    def test_list_agent_office_phone(self, source):
        '''and list_agent_office_phone are mapped with
FirstValueProvider:("agent_office_phone","office_phone")" '''
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                ListComponent(self.driver).get_list_agent_office_phone()
                actual = ListComponent(self.driver).get_txt_list_agent_office_phone()
                self.assertEqual(OFFICE_PHONE, actual)

    @parameterized.expand(sources)
    def test_list_agent_preferred_phone(self, source):
        ''' list_agent_preferred_phone are mapped with
FirstValueProvider:("agent_mobile_phone","agent_home_phone")'''
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                ListComponent(self.driver).get_list_agent_preferred_phone()
                actual = ListComponent(self.driver).get_txt_list_agent_preferred_phone()
                print(mls_id_dict.get(str(metadata)))
                self.assertEqual(PREFERRED_PHONE, actual)

    @parameterized.expand(sources)
    def test_mls_id_sa_id(self, source):
        '''Validate mls_source_id and sa_source_id are correct from here (NOT kw_id)'''
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                ListComponent(self.driver).get_list_sa_id()
                sa_id = ListComponent(self.driver).get_txt_ist_sa_id()
                mls_id = ListComponent(self.driver).get_txt_list_mls_id()
                actual = [mls_id, sa_id]
                target_list = mls_id_dict.get(source)
                mls_id_target = f'mls_id\n+\n[add]\n[add]\n[add]\n[add]\nSetConstant(const={target_list[0]},const_type=str)'
                sa_id_target = f'sa_source_id\n+\n[add]\n[add]\n[add]\n[add]\nSetConstant(const={target_list[1]},const_type=int)'
                target = [mls_id_target, sa_id_target]
                self.assertEqual(actual, target)

    @parameterized.expand(sources)
    def test_dashboard_source_number(self, source):
        '''Validate mls_id is the correct value from here'''
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        SourceSelectComponent(self.driver).get_select_wait().until(EC.invisibility_of_element_located(SOURCE_ID))
        SLPMain(self.driver).mls_btn_click()
        SLPMain(self.driver).ld_btn_click()
        DashBoard(self.driver).set_kw_source_id(source)
        DashBoard(self.driver).click_submit_btn()
        actual = DashBoard(self.driver).get_source_id_txt()
        self.assertEqual(actual, source)

    @parameterized.expand(sources)
    def test_currency_code(self, source):
        '''Currency_code must be UPPER'''
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                field = ListComponent(self.driver).get_txt_get_field('currency_code')
                match = re.search(r"const=([A-Za-z]{3})", field)
                if match:
                    currency_code = match.group(1)
                    is_upper = currency_code.isupper()
                self.assertTrue(is_upper)

    @parameterized.expand(sources)
    def test_list_dt(self, source):
        '''list_dt is mapped'''
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                field_actual = False
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                field = ListComponent(self.driver).get_txt_get_field('list_dt')
                if 'json_path=' in field:
                    field_actual = True
                print(field)
                self.assertTrue(field_actual)

    @parameterized.expand(sources)
    def test_raw_properties_list_status(self, source):
        '''raw.properties.list_status is mapped'''
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                field_actual = False
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                field = ListComponent(self.driver).get_txt_get_field('raw-properties-list_status')
                if 'json_path=' in field:
                    field_actual = True
                print(field)
                self.assertTrue(field_actual)

    @parameterized.expand(sources)
    def test_kww_region(self, source):
        ''' Kww_region has no mapping '''
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            with self.subTest(metadata=metadata):
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                expected_field = ListComponent(self.driver).get_expected_field('kww_region')
                actual_field = ListComponent(self.driver).get_txt_get_field('kww_region')
                self.assertEqual(actual_field, expected_field)

    @parameterized.expand(sources)
    def test_list_address_nullifier_const(self, source):
        '''Price_history must use PriceHistoryEnhancer with ListPrice input'''
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(SOURCE_ID))
        SLPMain(self.driver).source_select(source)
        metadata_numbers = ListComponent(self.driver).get_metadata_number()
        for metadata in range(1, metadata_numbers):
            actual = []
            with self.subTest(metadata=metadata):
                field_actual = False
                SLPMain(self.driver).metadata_main_select(metadata)
                SLPMain(self.driver).impl_wait_metadata()
                price_history = ListComponent(self.driver).get_txt_get_field('price_history')
                if 'json_path=' in price_history and 'PriceHistoryEnhancer' in price_history:
                    field_actual = True
                    actual.append(field_actual)
                else:
                    actual.append(field_actual)
                    print('price_history = ', field_actual)

                price_history_items = ListComponent(self.driver).get_txt_get_field('price_history-items')
                field_actual = False
                if 'ValueProvider(json_path=[],skip_values=[])' in price_history_items:
                    field_actual = True
                    actual.append(field_actual)
                else:
                    actual.append(field_actual)
                    print('price_history-items = ', field_actual)

                price_history_in_use = ListComponent(self.driver).get_txt_get_field(
                    'price_history-items-properties-in_use')
                field_actual = False
                if 'ValueProvider(json_path=in_use,skip_values=[])' in price_history_in_use:
                    field_actual = True
                    actual.append(field_actual)
                else:
                    actual.append(field_actual)
                    print('price_history-items-properties-in_use = ', field_actual)

                price_history_percent_change = ListComponent(self.driver).get_txt_get_field(
                    'price_history-items-properties-percent_change')
                field_actual = False
                if 'ValueProvider(json_path=percent_change,skip_values=[])' in price_history_percent_change:
                    field_actual = True
                    actual.append(field_actual)
                else:
                    actual.append(field_actual)
                    print('price_history.items.properties.percent_change = ', field_actual)

                price_history_update_at = ListComponent(self.driver).get_txt_get_field(
                    'price_history-items-properties-price_updated_at')
                field_actual = False
                if 'ValueProvider(json_path=price_updated_at,skip_values=[])' in price_history_update_at:
                    field_actual = True
                    actual.append(field_actual)
                else:
                    actual.append(field_actual)
                    print('price_history.items.properties.price_updated_at = ', field_actual)
                self.assertTrue(all(actual))

                price_history_current_list_price = ListComponent(self.driver).get_txt_get_field(
                    'price_history-items-properties-current_list_price')
                field_actual = False
                if 'ValueProvider(json_path=current_list_price,skip_values=[])' in price_history_current_list_price:
                    field_actual = True
                    actual.append(field_actual)
                else:
                    actual.append(field_actual)
                    print('price_history.items.properties.current_list_price = ', field_actual)

                price_history_previous_list_price = ListComponent(self.driver).get_txt_get_field(
                    'price_history-items-properties-previous_list_price')
                field_actual = False
                if 'ValueProvider(json_path=previous_list_price,skip_values=[])' in price_history_previous_list_price:
                    field_actual = True
                    actual.append(field_actual)
                else:
                    actual.append(field_actual)
                    print('price_history.items.properties.previous_list_price = ', field_actual)
                self.assertTrue(all(actual))
