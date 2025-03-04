import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from SLP.ui.Elements.button import Button
from SLP.ui.PageObjects.SLPMain.listing_component import ListComponent
from SLP.ui.PageObjects.SLPMain.madia_component import MediaComponent
from SLP.ui.PageObjects.SLPMain.source_select_component import SourceSelectComponent
from selenium.webdriver.support import expected_conditions as EC

from SLP.ui.base_page import BasePage

LISTING_TAB = (By.XPATH, '/html/body/section/div/div/div/div[1]/div/div/a[1]')
PHOTO_TAB = (By.XPATH, '/html/body/section/div/div/div/div[1]/div/div/a[2]')
SAVE_MAP_BTN = (By.CSS_SELECTOR, '#btn_save_map')
DATE_SAVE = (By.ID, 'last_edited')
IMPLIS_WAIT_MAP = (By.CSS_SELECTOR, '#listing_mapper_list_category__0')
IMPLIS_WAIT_MEDIA_MAP = (By.CSS_SELECTOR, '#photo_mapper_mls_number__0')
SOURCE_SELECT = (By.CSS_SELECTOR, '#sources')
SPINNER = (By.CSS_SELECTOR, '#spin_save_map')
MLS_BTN = (By.CSS_SELECTOR, '#navbarNav > ul.navbar-nav.me-auto.mb-2.mb-lg-0 > li:nth-child(2) > a')
LDBUTTON = (By.LINK_TEXT, "Listings Dashboard")

class SLPMain(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._ld_btn = None
        self._mls_btn = None
        self.webdriver = None
        self.get_text = None
        self.driver = driver
        self._photo_tub = None
        self._list_tub = None
        self.node = None
        self._source_selected = None

    @allure.step("Get save time")
    def get_save_time(self):
        return self.node.find_element(*DATE_SAVE)

    @allure.step("Get save time text")
    def text_save_time(self):
        self.get_text = self.get_save_time
        return self.get_save_time().text

    @allure.step("Source select")
    def source_select(self, source):
        SourceSelectComponent(self.driver).source_select(source)
        SourceSelectComponent(self.driver).click_apply_source_btn()

    @allure.step("Select main metadata")
    def metadata_main_select(self, metadata):

        list_component = ListComponent(self.driver)
        list_component.list_metadata_select(metadata)

    @allure.step("Scroll top")
    def scroll_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    @allure.step("Implicit wait metadata")
    def impl_wait_metadata(self):
        ListComponent(self.driver).get_map_filed(IMPLIS_WAIT_MAP)

    @allure.step("Implicit wait metadata")
    def impl_wait_media_metadata(self):
        MediaComponent(self.driver).get_map_filed(IMPLIS_WAIT_MEDIA_MAP)

    @allure.step("Wait until spinner available")
    def wait_until_spinner_available(self):
        return self.driver.get_select_wait().until(EC.presence_of_element_located((By.CSS_SELECTOR, "//*[@id='spin_save_map' and contains(@class, 'spinner-border') and not(contains(@class, 'd-none'))]")))

    @allure.step("Wait until spinner unavailable")
    def wait_until_spinner_unavailable(self):
        return self.driver.get_select_wait().until(EC.presence_of_element_located((By.CSS_SELECTOR, "//*[@id='spin_save_map' and contains(@class, 'spinner-border') and contains(@class, 'd-none')]")))

    @allure.step("Zoom window")
    def zoom_window(self):
        webdriver.ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.ADD).key_up(Keys.CONTROL).perform()
        self.driver.execute_script("document.body.style.zoom='60%'")

    @allure.step("Get MLS button")
    def get_mls_btn(self):
        node = self.driver.find_element(*MLS_BTN)
        self._mls_btn = Button(node)
        return self._mls_btn

    @allure.step("MLS button click")
    def mls_btn_click(self):
        return self.get_mls_btn().click_button()

    @allure.step("Get LD button")
    def get_ld_btn(self):
        node = self.driver.find_element(*LDBUTTON)
        self._ld_btn = Button(node)
        return self._ld_btn

    @allure.step("LD button click")
    def ld_btn_click(self):
        return self.get_ld_btn().click_button()
