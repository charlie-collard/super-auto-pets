import re
import json
from mitmproxy import http

battle_filename = 'generated-battle.json' # name of the file you generated with make_team.py
path = f'/path/to/your/{battle_filename}' # <---change this!!

def request(flow: http.HTTPFlow) -> None:
    if not (flow.request.method == "GET"):
        return
    if match := re.search("https://api.teamwoodgames.com/api/battle/get/([-a-f0-9]*)", flow.request.pretty_url):
        (battle_id,) = match.groups()
        with open(path) as f:
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

