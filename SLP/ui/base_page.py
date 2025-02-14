# import time
# import pyautogui
import time

import pyautogui
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from SLP.ui.Elements.button import Button
from SLP.ui.Elements.tab import Tub
from SLP.ui.PageObjects.SLPMain.listing_component import ListComponent
from SLP.ui.PageObjects.SLPMain.source_select_component import SourceSelectComponent
from selenium.webdriver.support import expected_conditions as EC

LISTING_TAB = (By.XPATH, '/html/body/section/div/div/div/div[1]/div/div/a[1]')
PHOTO_TAB = (By.XPATH, '/html/body/section/div/div/div/div[1]/div/div/a[2]')
SAVE_MAP_BTN = (By.CSS_SELECTOR, '#btn_save_map')
DATE_SAVE = (By.ID, 'last_edited')
IMPLIS_WAIT_MAP = (By.CSS_SELECTOR, '#listing_mapper_list_category__0')
SOURCE_SELECT = (By.CSS_SELECTOR, '#sources')
SPINNER = (By.CSS_SELECTOR, '#spin_save_map')
MLS_BTN = (By.CSS_SELECTOR, '#navbarNav > ul.navbar-nav.me-auto.mb-2.mb-lg-0 > li:nth-child(2) > a')
LDBUTTON = (By.LINK_TEXT, "Listings Dashboard")

class BasePage:
    def __init__(self, driver):
        self._ld_btn = None
        self._mls_btn = None
        self.webdriver = None
        self.get_text = None
        self.driver = driver
        self._photo_tub = None
        self._list_tub = None
        self.node = None
        self._source_selected = None

    def get_list_tub(self):
        node = self.driver.find_element(*LISTING_TAB)
        self._list_tub = Tub(node)
        return self._list_tub

    def select_list_tub(self):
        self.get_list_tub().select_tab()

    def get_photo_tub(self):
        node = self.driver.find_element(*PHOTO_TAB)
        self._photo_tub = Tub(node)
        return self._photo_tub

    def select_photo_tub(self):
        self.get_photo_tub().select_tab()

    def get_save_button(self) -> Button:
        self.driver.implicitly_wait(20)
        node = self.driver.find_element(*SAVE_MAP_BTN)
        self._photo_tub = Button(node)
        return self._photo_tub

    def click_save_button_(self):
        return self.get_save_button().click_button()

    def click_OK_button_(self):
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(1100, 230)
        time.sleep(1)
        pyautogui.click()