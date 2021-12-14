#!/usr/bin/env python3
import subprocess

out = subprocess.run(["networksetup", "-getsecurewebproxy", "Wi-Fi"], capture_output=True).stdout.decode("utf8")

enable = "on" if "Enabled: No" in out else "off"

subprocess.run(["networksetup", "-setsecurewebproxystate", "Wi-Fi", enable])

print("Proxy turned", enable)
