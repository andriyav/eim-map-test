import unittest
from data.test_data import sources
from parameterized import parameterized

from SLP.api.utils.api_request import APIrequest
from SLP.api.utils.config_name import ConfigName
from SLP.api.utils.dict_stage import DictStage


class TestApi(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.config_name = None
        self.mls_num = None

    @parameterized.expand(sources)
    def test_api(self, source):
        config_names = ConfigName.config_names(source)
        n = 0
        for config_name in config_names:
            n += 1
            with self.subTest(config_name=config_name):
                config = DictStage.get_dict_stage(config_name)
                query = config.get('template')
                response = APIrequest.get_request(query, config_name)
                if response.status_code == 200:
                    result = True
                else:
                    result = False
                self.assertTrue(result, response)
                print(f"\nConfig name: {config_name[0]}, Response code: {response.status_code}", flush=True)
