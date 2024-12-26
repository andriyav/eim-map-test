import time

from SLP.ui.PageObjects.SLPlogin.slp_login import LoginComponent
from SLP.ui.PageObjects.login_modal.login_modal import LoginModal
from data.value_provider import ValueProvider
from tests.test_runner import BaseTestRunner


class TestPromotionChecklist(BaseTestRunner):
    def test_screen(self):
        self.driver.get(ValueProvider.get_base_url())
        LoginComponent(self.driver).click_authorisation_btn()
        LoginModal(self.driver).set_email(ValueProvider.get_email())
        LoginModal(self.driver).click_next_button_first()
        LoginModal(self.driver).set_password(ValueProvider.get_password())
        LoginModal(self.driver).click_next_button_second()
        self.driver.maximize_window()
        time.sleep(5)
        self._take_screenshot('button_interaction_failed.png')


