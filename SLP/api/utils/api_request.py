import requests

from SLP.api.utils.dict_stage import DictStage
from data.value_provider import ValueProvider

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

class APIrequest:
    query = None

    @classmethod
    def get_request(cls, query, config_name):
        url = f"https://query.ampre.ca/odata/{query}"
        url = url.format(missing_listings=missing_listings, missing_offices=missing_offices, top=top,
                         previous_query_listing_keys=previous_query_listing_keys, skip_count=skip_count,
                         last_3_days=last_3_days,
                         modified_timestamp=modified_timestamp, last_30_days_date=last_30_days_date,
                         open_house_date=open_house_date,
                         missing_agents=missing_agents)
        feed = DictStage.get_dict_stage(config_name).get('name')[-1:]
        token_idx = ValueProvider.get_token_idx()
        token_vow = ValueProvider.get_token_vow()
        token_dla = ValueProvider.get_token_dla()
        token = "token_IDX"
        if feed in ("7", "2"):
            token = token_idx
        if feed in ("3", "4"):
            token = token_vow
        if feed in ("5", "6"):
            token = token_dla
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        return requests.get(url, headers=headers)