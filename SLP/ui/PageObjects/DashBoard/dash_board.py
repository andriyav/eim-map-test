from selenium.webdriver.common.by import By
from SLP.ui.Elements.button import Button
from SLP.ui.Elements.check_box import CheckBox
from SLP.ui.Elements.input import Input
from SLP.ui.PageObjects.base_components import BaseComponent

KW_SOURCE_ID = (By.CSS_SELECTOR, 'body > div.col-5.center > form > div:nth-child(1) > div:nth-child(1) > input')
SUBMIT_BTN = (By.CSS_SELECTOR, '#submit')
KW_SOURCE_ID_TXT = (By.XPATH, '/html/body/div[4]/div[3]/div[2]/table/tbody/tr[1]/td[5]')
VIEW_DATA = (By.XPATH, '/html/body/div[4]/div[3]/div[2]/table/tbody[1]/tr[2]/td[11]/p[4]')
PHOTO_CHECK = (
    By.CSS_SELECTOR, 'body > div.col-5.center > form > div:nth-child(2) > div:nth-child(3) > input[type=checkbox]')
OH_CHECK = (
    By.CSS_SELECTOR, 'body > div.col-5.center > form > div:nth-child(2) > div:nth-child(4) > input[type=checkbox]')
LIST_SOURCES = (By.CSS_SELECTOR, "table#listings tbody tr")
KW_ID_INPUT = (By.CSS_SELECTOR, "body > div.col-5.center > form > div:nth-child(1) > div:nth-child(3) > input")
VIEW_DATA_SINGLE = (By.XPATH, "/html/body/div[4]/div[3]/div[2]/table/tbody[1]/tr/td[11]/p[4]")
KW_ID = (By.XPATH, "/html/body/div[4]/div[3]/div[2]/table/tbody[1]/tr[1]/td[4]")


class DashBoard(BaseComponent):
    def __init__(self, node):
        super().__init__(node)
        self._kw_id_input = None
        self._view_data_btn_single = None
        self._mls_input = None
        self._oh_check_box = None
        self._phot_check_box = None
        self._view_data_btn = None
        self._submit_btn = None
        self._source_input = None

    def get_source_input(self):
        if not self._source_input:
            node = self.node.find_element(*KW_SOURCE_ID)
            self._source_input = Input(node)
        return self._source_input

    def set_kw_source_id(self, source: str):
        # set source mls_id"
        self.get_source_input().set_text(source)
        return self

    def get_kw_id_input(self):
        if not self._kw_id_input:
            node = self.node.find_element(*KW_ID_INPUT)
            self._kw_id_input = Input(node)
        return self._kw_id_input

    def set_kwid(self, kw_id: str):
        # set source KW_ID"
        self.get_kw_id_input().set_text(kw_id)

    def get_submit_btn(self):
        node = self.node.find_element(*SUBMIT_BTN)
        self._submit_btn = Button(node)
        return self._submit_btn

    def click_submit_btn(self):
        # Click submit button in Dash Board.
        self.get_submit_btn().click_button()

    def get_source_id_txt(self):
        return self.node.find_element(*KW_SOURCE_ID_TXT).text

    def get_view_data_btn(self):
        node = self.node.find_element(*VIEW_DATA)
        self._view_data_btn = Button(node)
        return self._view_data_btn

    def click_view_data_btn(self):
        self.get_view_data_btn().click_button()

    def get_photo_check_box(self):
        node = self.node.find_element(*PHOTO_CHECK)
        self._phot_check_box = CheckBox(node)
        return self._phot_check_box

    def select_photo_check_box(self):
        return self.get_photo_check_box().select_check_box()

    def get_oh_check_box(self):
        node = self.node.find_element(*OH_CHECK)
        self._oh_check_box = CheckBox(node)
        return self._oh_check_box

    def select_oh_check_box(self):
        return self.get_oh_check_box().select_check_box()

    def get_list_of_sources(self):
        return self.node.find_elements(*LIST_SOURCES)

    def get_view_data_btn_single(self):
        node = self.node.find_element(*VIEW_DATA_SINGLE)
        self._view_data_btn_single = Button(node)
        return self._view_data_btn_single

    def click_view_data_btn_single(self):
        self.get_view_data_btn_single().click_button()

    def get_kw_id_txt(self):
        return self.node.find_element(*KW_ID).text
