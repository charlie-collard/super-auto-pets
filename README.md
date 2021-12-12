# Super Auto Pets replay editor

A tool to allow for viewing of arbitrary Super Auto Pets replays

### Requirements

* Install [python 3](https://www.python.org/downloads/)
* Install [mitmproxy](https://docs.mitmproxy.org/stable/overview-installation/)
* Install [mitmproxy's root certificate](https://docs.mitmproxy.org/stable/concepts-certificates/) on your computer - ⚠️  _You must keep the private key for this certificate safe_! Anyone who gets a hold of it will gain the ability to intercept **all of your traffic on the web**. I would recommend uninstalling the certificate when you are not using mitmproxy.

### Usage

1. Open [Super Auto Pets](https://teamwood.itch.io/super-auto-pets) in your browser, start a game, and get to the point where you can watch a replay (the swords in the top right).
2. Edit `team_1` and `team_2` in `make-team.py` to your desired teams
3. Run `python3 make-team.py`
4. Start the proxy with `./start-proxy.sh`
5. Configure your browser to use the proxy
6. Press the replay button in-game. It should play out the replay.
