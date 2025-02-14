
from colorama import Fore, init
from pathlib import Path

from SLP.api.utils.query import DBHandler
from utils.db_access import DBAccess
import requests
init()
mls_num = 387
top = 200
count = 'true'
modified_timestamp = '2023-03-04T20:32:04.00Z'

# mls_num = 80
def api_queries():
    init()
    mls_num = 387
    top = 200
    missing_listings = "ListingKey eq 'S10437676'"
    missing_offices = "OfficeKey eq '270600'"
    previous_query_listing_keys = "ResourceRecordKey eq 'S10437676'"
    skip_count = "1"
    last_3_days = '2023-03-04T20:32:04.00Z'
    modified_timestamp = '2023-03-04T20:32:04.00Z'
    last_30_days_date = '2023-03-04'
    open_house_date = '2023-03-04'
    missing_agents = "MemberKey eq '9647938'"
    global dict_stage
    folder_path = Path("./")
    json_files = folder_path.glob("*.json")
    for file_path in json_files:
        file_path.unlink()
    con = con = DBAccess.db_access_stage_mls_admin()
    cur = con.cursor()
    cur.execute(DBHandler.config_downloads_names(mls_num))
    config_names = cur.fetchall()
    cur.close()
    con.close()
    n = 0
    list_failed = []
    for config_name in config_names:
        n += 1
        config_name = config_name[0]
        con = DBAccess.db_access_stage_mls_admin()
        cur = con.cursor()
        cur.execute(DBHandler.config_downloads_queries(mls_num, config_name))
        result_stage = cur.fetchone()
        if config_name is None:
            print(Fore.LIGHTYELLOW_EX + "It seems the RETS source is under testing. "
                                        "The tool does not support configuration comparison for RETS sources.")
            break
        dict_stage = {
            "name": result_stage[0],
            "config": result_stage[1],
            "secrets": result_stage[2],
            "query_params": result_stage[3],
            "template": result_stage[4],
            "custom_config": result_stage[5]
        }
        cur.close()
        con.close()
        query = dict_stage.get('template')
        url = f"https://query.ampre.ca/odata/{query}"
        url = url.format(missing_listings=missing_listings, missing_offices=missing_offices, top=top,
                         previous_query_listing_keys=previous_query_listing_keys, skip_count=skip_count, last_3_days=last_3_days,
                         modified_timestamp = modified_timestamp, last_30_days_date=last_30_days_date, open_house_date=open_house_date,
                         missing_agents=missing_agents)
        feed = dict_stage.get('name')[-1:]
        token_IDX = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ2ZW5kb3IvdHJyZWIvMzM5NCIsImF1ZCI6IkFtcFVzZXJzUHJkIiwicm9sZXMiOlsiQW1wVmVuZG9yIl0sImlzcyI6InByb2QuYW1wcmUuY2EiLCJleHAiOjI1MzQwMjMwMDc5OSwiaWF0IjoxNzI4NTAyMzA3LCJzdWJqZWN0VHlwZSI6InZlbmRvciIsInN1YmplY3RLZXkiOiIzMzk0IiwianRpIjoiNTg4ZjUzMWU2ZGY2NWM5ZCIsImN1c3RvbWVyTmFtZSI6InRycmViIn0.1x0ror22cmQcX7bKOUKL79-autc_e-mLhTBwJ6VC6vc"
        token_VOW = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ2ZW5kb3IvdHJyZWIvMzM5NCIsImF1ZCI6IkFtcFVzZXJzUHJkIiwicm9sZXMiOlsiQW1wVmVuZG9yIl0sImlzcyI6InByb2QuYW1wcmUuY2EiLCJleHAiOjI1MzQwMjMwMDc5OSwiaWF0IjoxNzI4NTAyNDk3LCJzdWJqZWN0VHlwZSI6InZlbmRvciIsInN1YmplY3RLZXkiOiIzMzk0IiwianRpIjoiYjcxOGE1NTUyMzU3OTdlYSIsImN1c3RvbWVyTmFtZSI6InRycmViIn0.93RGRYF32wHF3tyMo7EwJ_maupIeujau9e-mxs7_UHU"
        token_DLA = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ2ZW5kb3IvdHJyZWIvMzM5NCIsImF1ZCI6IkFtcFVzZXJzUHJkIiwicm9sZXMiOlsiQW1wVmVuZG9yIl0sImlzcyI6InByb2QuYW1wcmUuY2EiLCJleHAiOjI1MzQwMjMwMDc5OSwiaWF0IjoxNzI4NTAyNTUyLCJzdWJqZWN0VHlwZSI6InZlbmRvciIsInN1YmplY3RLZXkiOiIzMzk0IiwianRpIjoiYjhhMThjYTlhMjE1NDVlYSIsImN1c3RvbWVyTmFtZSI6InRycmViIn0.7tz-FzrRSFR4M8wcwwbvGTZqHXmCzvguU8td0dRJPuE"
        token = "token_IDX"
        if feed in ("7", "2"):
            token = token_IDX
            feed_name = "IDX"
        if feed in ("3", "4"):
            token = token_VOW
            feed_name = "VOW"
        if feed in ("5", "6"):
            token = token_DLA
            feed_name = "DLA"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                print(n,". ", "ok", response.status_code, feed_name, " ", dict_stage.get('name'), " ",  url)
            else:
                list_failed.append(n)
                print(n,". ", "Failed to retrieve data. Status code:", response.status_code, feed_name, " ", url,)
        except:
            list_failed.append(n)
            print(n,". ", "wrong query", feed_name, " ", url,)
    print(list_failed)

api_queries()