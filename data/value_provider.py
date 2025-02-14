import os
from dotenv import load_dotenv
BASE_URL = 'https://stage-slp.data.kw.com/login'
BASE_URL_PROD = 'https://prod-slp.data.kw.com/login'
load_dotenv()


class ValueProvider:
    @classmethod
    def get_email(cls):
        return os.getenv("EMAIL")

    @classmethod
    def get_password(cls) -> str:
        return os.getenv("PASSWORD")

    @classmethod
    def get_token_IDX(cls) -> str:
        return os.getenv("PASSWORD")

    @classmethod
    def get_token_VOW(cls) -> str:
        return os.getenv("PASSWORD")

    @classmethod
    def get_token_DLA(cls) -> str:
        return os.getenv("PASSWORD")
    @classmethod
    def get_base_url(cls):
        return BASE_URL


    @classmethod
    def get_mls_id(cls):
        sources = [
            "19"
        ]
        return sources

    @classmethod
    def get_mapping_configuration(cls):
        config = {
            "field": "is_short_sale",
            "MappersProvider": 6,
            "Metadata": "SpecialListingConditions",
            "Rules": 413,
            "Enhancers": 33,
            "Const": "False"
        }
        return config



