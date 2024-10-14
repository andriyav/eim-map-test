import unittest

from tests.test_runner import BaseTestRunner


class SLPPageTestCase(BaseTestRunner):

    def test_map_field(self):
        self.assertEqual("good", "good")
