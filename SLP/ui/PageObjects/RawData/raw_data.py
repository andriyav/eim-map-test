
from selenium.webdriver.common.by import By
from SLP.ui.Elements.tab import Tub
from SLP.ui.PageObjects.base_components import BaseComponent

PHOTONUM = (
    By.XPATH, '/html/body/div[4]/div[3]/div[2]/table/tbody[1]/tr[1]/td[11]/div/div/div/div/div[1]/div/div/ul/li[68]/ul')
RAW_DATA_TUB = (By.XPATH, '/html/body/div[4]/div[3]/div[2]/table/tbody/tr[2]/td[11]/div/div/div/nav/div/a[1]')
RAW_DATA_TUB_SINGLE = (By.XPATH,'/html/body/div[4]/div[3]/div[2]/table/tbody/tr/td[11]/div/div/div/nav/div/a[1]')
PHOTO_NUM = (By.XPATH,
             "//a[contains(@class, 'prop') and contains(., 'photos')]/following-sibling::ul[@class='array level1 collapsible']")
PHOTO_COUNT = (By.XPATH, "//a[@class='prop' and contains(., 'mls_media_count')]/following-sibling::span[@class='num']")
KEY = "a1917370853664640a"
BROKERAGE_COLLAPSE = (
    By.XPATH, "//li[.//a[@class='prop' and contains(., 'brokerage')]]]")


class RawData(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._brokerage_collapse = None
        self.parent_div = None
        self._raw_data_tub = None

    def get_raw_data_tub(self):
        node = self.node.find_element(*RAW_DATA_TUB)
        self._raw_data_tub = Tub(node)
        return self._raw_data_tub

    def click_raw_data_tub(self):
        self.get_raw_data_tub().select_tab()

    def get_raw_data_tub_single(self):
        node = self.node.find_element(*RAW_DATA_TUB_SINGLE)
        self._raw_data_tub = Tub(node)
        return self._raw_data_tub

    def click_raw_data_tub__single(self):
        self.get_raw_data_tub_single().select_tab()

    def get_photo_count(self):
        parent_element = self.node.find_element(
            By.XPATH, "//a[contains(text(), 'mls_media_count')]/../span[@class='num']")
        result = self.node.execute_script('return arguments[0].textContent;', parent_element)
        return result


    def get_marketing_info_collapse(self, value):
        # Locate the parent element containing 'marketing_info'
        parent_kw_updated_by = self.node.find_element(By.XPATH,
                                                      "//a[contains(text(), 'marketing_info')]/ancestor::li")

        # Locate the nested 'ul' element with the specified class
        span_element_kw_updated_by = parent_kw_updated_by.find_element(By.XPATH,
                                                                       ".//ul[@class='obj level1 collapsible']")

        # Locate the 'bool' span element following 'display_address'
        next_element = span_element_kw_updated_by.find_element(By.XPATH,
                                                               f".//a[contains(text(), '{value}')]/following-sibling::span[@class='bool']")

        # Extract the text content using JavaScript and print the result
        return self.node.execute_script('return arguments[0].textContent;', next_element)

    def get_kwls_status(self):

        parent_element = self.node.find_element(
            By.XPATH, "//a[contains(text(), 'kwls_status')]/../span[@class='string']")
        result = self.node.execute_script('return arguments[0].textContent;', parent_element)
        return result

    def get_photo_number(self):
        photo_link = self.node.find_element(By.XPATH, "//a[contains(text(), 'photos')]")
        span_element_list_address = photo_link.find_elements(By.XPATH, '//ul[@class="array level1 collapsible"]')
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
