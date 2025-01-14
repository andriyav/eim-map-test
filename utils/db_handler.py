import psycopg2
from utils.db_access import DBAccess


# run tunel slp5 tunnel cloudsql prod postgres-agent-office

class DBHandler:

    @classmethod
    def db_handler(cls, source, mls_agent, mls_office):
        con = DBAccess.db_access_prod()
        cur = con.cursor()
        cur.execute(f''' select *
        from mls_agent ma
        where kw_mls_id = {source}
        and mls_id_1_str = '{mls_agent}'
        ''')
        agent_id = ''
        data_agent = cur.fetchall()
        for unit in data_agent:
            agent_id = unit[0]

        cur.execute(f''' select *
        from mls_office mo
        where kw_mls_id = {source}
        and mls_id_1_str = '{mls_office}'
        ''')
        office_id = ''
        data_office = cur.fetchall()
        for unit in data_office:
            office_id = unit[0]
        try:
            cur.execute(f''' select *
            from agent_office ao
            where agent_id = {agent_id}
            and agent_id = {agent_id}
            and office_id = {office_id}
            
            ''')
            return True
        except:
            return False

