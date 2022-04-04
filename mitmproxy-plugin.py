import re
import json
from mitmproxy import http

battle_filename = "generated-battle.json"
api_version = "0.17"
beta_api_version = "0.18"


def request(flow: http.HTTPFlow) -> None:
    if not (flow.request.method == "GET"):
        return
    if battle_id := is_valid_battle_url(flow.request.pretty_url):
        with open(battle_filename) as f:
            data = json.load(f)
        data["Id"] = battle_id
        flow.response = http.Response.make(
            200,
            bytes(json.dumps(data), encoding="utf8"),
            {
                "Content-Type": "application/json; charset=utf-8",
                "Access-Control-Allow-Origin": "*"
            }
        )


def is_valid_battle_url(url) -> str:
    battle_id = ""
    if match := re.search(f"https://api.teamwood.games/{api_version}/api/battle/get/([-a-f0-9]*)", url):
        (battle_id,) = match.groups()
    elif match := re.search(f"https://staging.teamwood.games/{beta_api_version}/api/battle/get/([-a-f0-9]*)", url):
        (battle_id,) = match.groups()

    return battle_id
