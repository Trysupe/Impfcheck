#!/usr/bin/env python3

import requests
import json
from pprint import pprint



url = "https://impfterminradar.de/api/vaccinations/availability"
head = {
    "Accept": "application/json"
}

with open("patch.json") as f:
    data = json.load(f)

r = requests.patch(url, json=data, headers=head)
result = r.json()
pprint(result)

available = [x for x in result if x["Available"] ]

pprint(available)