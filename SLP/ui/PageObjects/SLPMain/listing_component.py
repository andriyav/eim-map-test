from selenium.webdriver.common.by import By

from SLP.ui.Elements.select import Select
from SLP.ui.PageObjects.base_components import BaseComponent

METADATA_SELECT = (By.XPATH, '//*[@id="metadataSelect"]')
COUNTRY = (By.XPATH, '/html/body/section/div/div/div/div[1]/div/form/div[6]/div/div/table/tbody/tr[83]')
CO_LIST_OFFICE_PHONE = (By.CSS_SELECTOR,
                        '#nav-home > div > table > tbody > tr.master_schema.kw_listing.co_list_agent_office-properties-co_list_agent_office_phone')
CO_LIST_PREFERRED_PHONE = (By.CSS_SELECTOR,
                           '#nav-home > div > table > tbody > tr.master_schema.kw_listing.co_list_agent_office-properties-co_list_agent_preferred_phone')
LIST_OFFICE_PHONE = (By.CSS_SELECTOR,
                     '#nav-home > div > table > tbody > tr.master_schema.kw_listing.list_agent_office-properties-list_agent_office_phone')
LIST_PREFERRED_PHONE = (By.CSS_SELECTOR,
                        '#nav-home > div > table > tbody > tr.master_schema.kw_listing.list_agent_office-properties-list_agent_preferred_phone')
LIST_MLS_ID = (By.CSS_SELECTOR, '#nav-home > div > table > tbody > tr.master_schema.kw_listing.required.mls_id')
LIST_SA_ID = (By.CSS_SELECTOR, '#nav-home > div > table > tbody > tr.master_schema.kw_listing.required.sa_source_id')
UNMAPPED_CLASS = (By.CSS_SELECTOR, 'body > div.flashes.container')







class ListComponent(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self.mapper_selector = None
        self._source_selected = None

    def get_list_metadata_select(self):
        node = self.node.find_element(*METADATA_SELECT)
        self._source_selected = Select(node)
        return self._source_selected

    def get_metadata_number(self):
        elements = self.get_list_metadata_select().get_options()
        return len(elements)

    def list_metadata_select(self, metadata):
        return self.get_list_metadata_select().set_select_by_index(metadata)

    def get_metadata_for_text(self, metadata):
        return self.node.find_element(By.XPATH, f'// *[ @ id = "metadataSelect"] / option[{metadata}]')

    def get_metadata_text(self, metadata):
        return self.get_metadata_for_text(metadata).text

    def get_map_filed(self, xpath):
        return self.node.find_element(*xpath)

    def get_list_address_country(self):
        return self.node.find_element(*COUNTRY)

    def get_txt_list_address_country(self):
        return self.get_list_address_country().text

    def get_co_list_agent_office_phone(self):
        return self.node.find_element(*CO_LIST_OFFICE_PHONE)

    def get_txt_co_list_agent_office_phone(self):
        return self.get_co_list_agent_office_phone().text

    def get_co_list_agent_preferred_phone(self):
        return self.node.find_element(*CO_LIST_PREFERRED_PHONE)

    def get_txt_co_list_agent_preferred_phone(self):
        return self.get_co_list_agent_preferred_phone().text

    def get_list_agent_office_phone(self):
        return self.node.find_element(*LIST_OFFICE_PHONE)

    def get_txt_list_agent_office_phone(self):
        return self.get_list_agent_office_phone().text

    def get_list_agent_preferred_phone(self):
        return self.node.find_element(*LIST_PREFERRED_PHONE)

    def get_txt_list_agent_preferred_phone(self):
        return self.get_list_agent_preferred_phone().text

    def get_list_mls_id(self):
        return self.node.find_element(*LIST_MLS_ID)

    def get_txt_list_mls_id(self):
        return self.get_list_mls_id().text

    def get_list_sa_id(self):
        return self.node.find_element(*LIST_SA_ID)

    def get_txt_ist_sa_id(self):
        return self.get_list_sa_id().text

    def get_field(self, field):
        return self.node.find_element(By.CSS_SELECTOR,
                                      f'#nav-home > div > table > tbody > tr.master_schema.kw_listing.{field}')

    def get_txt_get_field(self, field):
        return self.get_field(field).text

    def get_unmapped(self):
        return self.node.find_element(*UNMAPPED_CLASS)

    def get_unmapped_txt(self):
        return self.get_unmapped().text

    def get_expected_field(self, field):
        return \
            f"""{field}
+
[add]
[add]
[add]
[add]"""
