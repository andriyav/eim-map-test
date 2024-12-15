from selenium.webdriver.common.by import By

from SLP.ui.Elements.select import Select
from SLP.ui.PageObjects.base_components import BaseComponent

METADATA_SELECT = (By.XPATH, '//*[@id="metadataSelect"]')
COUNTRY = (By.XPATH,'/html/body/section/div/div/div/div[1]/div/form/div[6]/div/div/table/tbody/tr[83]')
CO_LIST_OFFICE_PHONE = (By.CSS_SELECTOR, '#nav-home > div > table > tbody > tr.master_schema.kw_listing.co_list_agent_office-properties-co_list_agent_office_phone')
CO_LIST_PREFERRED_PHONE = (By.CSS_SELECTOR, '#nav-home > div > table > tbody > tr.master_schema.kw_listing.co_list_agent_office-properties-co_list_agent_preferred_phone')
LIST_OFFICE_PHONE = (By.CSS_SELECTOR, '#nav-home > div > table > tbody > tr.master_schema.kw_listing.list_agent_office-properties-list_agent_office_phone')
LIST_PREFERRED_PHONE = (By.CSS_SELECTOR, '#nav-home > div > table > tbody > tr.master_schema.kw_listing.list_agent_office-properties-list_agent_preferred_phone')


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





