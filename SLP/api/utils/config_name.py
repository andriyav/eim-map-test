from pathlib import Path

from SLP.api.utils.query import DBHandler
from utils.db_access import DBAccess


class ConfigName:

    @classmethod
    def config_names(cls, mls_num):
        folder_path = Path("./")
        json_files = folder_path.glob("*.json")
        for file_path in json_files:
            file_path.unlink()
        con = DBAccess.db_access_stage_mls_admin()
        cur = con.cursor()
        cur.execute(DBHandler.config_downloads_names(mls_num))
        return cur.fetchall()
