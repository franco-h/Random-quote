#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/no"

resp = requests.get(URL).json()

# Take the JSON object and print it in the following format:
print(f"Good Choice! {resp['reason']}")
