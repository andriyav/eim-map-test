import os
from dotenv import load_dotenv

load_dotenv()


class ValueProvider:
    @classmethod
    def get_email(cls):
        return os.getenv("EMAIL")

    @classmethod
    def get_password(cls) -> str:
        return os.getenv("PASSWORD")

    @classmethod
    def get_base_url(cls):
        return os.getenv("BASE_URL")

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



