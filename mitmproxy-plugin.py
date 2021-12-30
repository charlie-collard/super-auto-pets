import re
import json
from mitmproxy import http

battle_filename = "generated-battle.json"

def request(flow: http.HTTPFlow) -> None:
    if not (flow.request.method == "GET"):
        return
    if match := re.search("https://api.teamwoodgames.com/v15/api/battle/get/([-a-f0-9]*)", flow.request.pretty_url):
        (battle_id,) = match.groups()
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

