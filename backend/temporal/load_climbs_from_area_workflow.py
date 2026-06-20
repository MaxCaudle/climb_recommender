from datetime import timedelta
from typing import Any, Optional

import requests
from temporalio import workflow, activity

def build_8a_url_for_area(country: str, location: str, page: int | str = 0) -> str:
    url = (f"https://www.8a.nu/api/unification/outdoor/v1/web/zlaggables/bouldering/"
           f"{country}?"
           f"sectorSlug&"
           f"pageIndex={page}&"
           f"sortField=totalascents&"
           f"grade&"
           f"searchQuery&"
           f"order=desc&"
           f"cragSlug={location}")
    return url


@activity.defn
async def get_climbs_for_page(country: str, location: str, page: int) -> dict[str, Any]:
    """
    """

    url = build_8a_url_for_area(country, location, page)
    resp: requests.Response = requests.get(url)

    return resp.json()

@activity.defn
def get_all_climbs_for_area(country: str, location: str) -> list[dict[str, Any]]:
    climbs: list[dict[str, int | str]] = []
    page: int = 0
    while True:
        resp_dict: dict[str, Any] = get_climbs_for_page(country, location, page)
        climbs += resp_dict["items"]
        if resp_dict.get("pagination", {}).get("hasNext"):
            page += 1
        else:
            return climbs



@workflow.defn
class LoadClimbsFromAreaWorkflow:
    @workflow.run
    async def run(self, location: str, climb: str):

        # Execute the LLM activity with a 300s timeout
        all_climbs: list[dict[str, Any]] = await workflow.execute_activity(
            get_all_climbs_for_area,
            location,
            climb,
            start_to_close_timeout=timedelta(seconds=300),
        )

        print(all_climbs)


