import time

from tests.test_runner import BaseTestRunner


class TestPromotionChecklist(BaseTestRunner):
    def test_screen(self):
        self._take_screenshot('button_interaction_failed.png')
        time.sleep(60)
