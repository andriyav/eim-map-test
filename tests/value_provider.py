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
