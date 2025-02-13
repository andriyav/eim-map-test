from selenium.webdriver.common.by import By
from SLP.ui.Elements.tab import Tub
from SLP.ui.PageObjects.base_components import BaseComponent

RAW_DATA_TUB = (By.XPATH, '/html/body/div[4]/div[3]/div[2]/table/tbody/tr[2]/td[11]/div/div/div/nav/div/a[1]')
RAW_DATA_TUB_SINGLE = (By.XPATH, '/html/body/div[4]/div[3]/div[2]/table/tbody/tr/td[11]/div/div/div/nav/div/a[1]')
PHOTO_NUM = (By.XPATH,
             "//a[contains(@class, 'prop') and contains(., 'photos')]/following-sibling::ul[@class='array level1 collapsible']")
PHOTO_COUNT = (By.XPATH, "//a[@class='prop' and contains(., 'mls_media_count')]/following-sibling::span[@class='num']")
PHOTO_TEXT = (By.XPATH, "//a[contains(text(), 'photos')]")
MARKETING_IFO = (By.XPATH, "//a[contains(text(), 'marketing_info')]/ancestor::li")
LIST_ADDRESS = (By.XPATH, "//a[contains(text(), 'list_address')]/ancestor::li")
MEDIA_COUNT = (By.XPATH, "//a[contains(text(), 'mls_media_count')]/../span[@class='num']")
COLLAPSIBLE = (By.XPATH, ".//ul[@class='obj level1 collapsible']")
COLLAPSIBLE_LEVEL1 = (By.XPATH, '//ul[@class="array level1 collapsible"]')
LIST_AGENT_OFFICE = (By.XPATH, "//a[contains(text(), 'list_agent_office')]/ancestor::li")
COLLAPSIBLE_AO = (By.XPATH, ".//ul[@class='obj level1 collapsible']")
# COLLAPSIBLE_LEVEL1_AO = '//ul[@class="array level1 collapsible"]'


class RawData(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self.parent_div = None
        self._raw_data_tub = None

    def get_raw_data_tub(self):
        node = self.node.find_element(*RAW_DATA_TUB)
        self._raw_data_tub = Tub(node)
        return self._raw_data_tub

    def click_raw_data_tub(self):
        # choose raw data tab in dashboard
        self.get_raw_data_tub().select_tab()

    def get_raw_data_tub_single(self):
        node = self.node.find_element(*RAW_DATA_TUB_SINGLE)
        self._raw_data_tub = Tub(node)
        return self._raw_data_tub

    def click_raw_data_tub__single(self):
        # Select the Raw Data tab in the dashboard if a single listing is selected.
        self.get_raw_data_tub_single().select_tab()

    def get_photo_count(self):
        # The method returns the value of media_count on the dashboard.
        parent_element = self.node.find_element(*MEDIA_COUNT)
        result = self.node.execute_script('return arguments[0].textContent;', parent_element)
        return result

    def get_marketing_info_collapse(self, value):
        # The method returns the value of marketing_info fields.
        # Locate the parent element containing 'marketing_info'
        parent_kw_updated_by = self.node.find_element(*MARKETING_IFO)

        # Locate the nested 'ul' element with the specified class
        span_element_kw_updated_by = parent_kw_updated_by.find_element(*COLLAPSIBLE)

        # Locate the 'bool' span element following 'display_address'
        next_element = span_element_kw_updated_by.find_element(By.XPATH,
                                                               f".//a[contains(text(), '{value}')]/following-sibling::span[@class='bool']")

        # Extract the text content using JavaScript and print the result
        return self.node.execute_script('return arguments[0].textContent;', next_element)

    def get_photo_number(self):
        # The method returns length of the list with photo URLs.
        photo_link = self.node.find_element(*PHOTO_TEXT)
        span_element_list_address = photo_link.find_elements(*COLLAPSIBLE_LEVEL1)
        outer = []
        indexes = []
        for i in span_element_list_address:
            outer_element = i.get_attribute("outerHTML")
            long = len(outer_element)
            indexes.append(long)
            outer.append(outer_element)
        maximum_len = max(indexes)
        index_max = indexes.index(maximum_len)
        result = str(outer[index_max].count('+'))
        return result

    def get_list_agent_office(self, value):
        # The method returns the value of list_agent_office".
        # Locate the parent element containing 'list_agent_office"o'
        parent_kw_updated_by = self.node.find_element(*LIST_AGENT_OFFICE)

        # Locate the nested 'ul' element with the specified class
        span_element_kw_updated_by = parent_kw_updated_by.find_element(*COLLAPSIBLE_AO)

        # Locate the 'bool' span element following 'display_address'
        next_element = span_element_kw_updated_by.find_element(By.XPATH,
                                                               f".//a[contains(text(), '{value}')]/following-sibling::span[@class='string']")
        # Extract the text content using JavaScript and print the result
        return self.node.execute_script('return arguments[0].textContent;', next_element)

    def get_list_address(self, value):
        # The method returns the value of get_list_address fields.
        # Locate the parent element containing 'marketing_info'
        parent = self.node.find_element(*LIST_ADDRESS)

        # Locate the nested 'ul' element with the specified class
        span_element = parent.find_element(*COLLAPSIBLE)

        # Locate the 'bool' span element following 'display_address'
        next_element = span_element.find_element(By.XPATH,
                                                 f".//a[contains(text(), '{value}')]/following-sibling::span[@class='string']")

        # Extract the text content using JavaScript and print the result
        return self.node.execute_script('return arguments[0].textContent;', next_element)
