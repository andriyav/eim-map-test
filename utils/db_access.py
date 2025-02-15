import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class DBAccess:

    @classmethod
    def db_access_stage(cls):
        return psycopg2.connect(
            host=os.getenv('HOST_STAGE'),
            port=os.getenv('PORT'),
            database=os.getenv('DATABASE'),
            user=os.getenv('USER_STAGE'),
            password=os.getenv('PASSWORD_STAGE')
        )

    @classmethod
    def db_access_stage_mls_admin(cls):
        return psycopg2.connect(
            host=os.getenv('HOST_STAGE'),
            port=os.getenv('PORT'),
            database=os.getenv('DATABASE_MLS_ADMIN'),
            user=os.getenv('USER_STAGE'),
            password=os.getenv('PASSWORD_STAGE')
        )
