from mitmproxy import http
import re
import json


def request(flow: http.HTTPFlow) -> None:
    if not (flow.request.method == "GET"):
        return
    if match := re.search("https://api.teamwoodgames.com/api/battle/get/([-a-f0-9]*)", flow.request.pretty_url):
        (battle_id,) = match.groups()
        with open("/Users/charlie/workspace/super-auto-pets/generated-battle.json") as f:
            data = json.load(f)
        data["Id"] = battle_id
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            bytes(json.dumps(data), encoding="utf8"),  # (optional) content
            {
                "Content-Type": "application/json; charset=utf-8",
                "Access-Control-Allow-Origin": "*"
            }
        )

