import time
import pyautogui
from selenium.webdriver.common.by import By
from SLP.ui.Elements.button import Button
from SLP.ui.Elements.tab import Tub

LISTING_TAB = (By.XPATH, '/html/body/section/div/div/div/div[1]/div/div/a[1]')
PHOTO_TAB = (By.XPATH, '/html/body/section/div/div/div/div[1]/div/div/a[2]')
SAVE_MAP_BTN = (By.CSS_SELECTOR, '#btn_save_map')

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