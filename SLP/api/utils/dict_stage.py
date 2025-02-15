from SLP.api.utils.query import DBHandler
from utils.db_access import DBAccess


class DictStage:

    @classmethod
    def get_dict_stage(cls, config_name):
        config_name = config_name[0]
        con = DBAccess.db_access_stage_mls_admin()
        cur = con.cursor()
        cur.execute(DBHandler.config_downloads_queries(config_name))
        result_stage = cur.fetchone()
        if config_name is None:
            print("It seems the RETS source is under testing. "
                  "The tool does not support configuration comparison for RETS sources.")
        return {
            "name": result_stage[0],
            "config": result_stage[1],
            "secrets": result_stage[2],
            "query_params": result_stage[3],
            "template": result_stage[4],
            "custom_config": result_stage[5]
        }
