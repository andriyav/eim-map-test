import psycopg2
from utils.db_access import db_access_prod

#slp5 tunnel cloudsql prod postgres-agent-office

con = db_access_prod()
source = 220
DATE_STRING_CONST = "2023-06-08"
date_str = DATE_STRING_CONST
cur = con.cursor()

cur.execute(f''' select *
from mls_agent ma
where kw_mls_id = {source}
and mls_id_1_str = '440002441'
''')
agent_id = ''
data_agent = cur.fetchall()
for unit in data_agent:
    agent_id = unit[0]
print(agent_id, 'agent_id')

cur.execute(f''' select *
from mls_office mo
where kw_mls_id = {source}
and mls_id_1_str = 'l001120'
''')
office_id = ''
data_office = cur.fetchall()
for unit in data_office:
    office_id = unit[0]
print(office_id,"office_id")

cur.execute(f''' select *
from agent_office ao
where agent_id = {agent_id}
and agent_id = {agent_id}
and office_id = {office_id}

''')
agent_office_id = ''
agent_office = cur.fetchall()
for unit in agent_office:
    agent_office_id = unit[0]
print(agent_office_id)
