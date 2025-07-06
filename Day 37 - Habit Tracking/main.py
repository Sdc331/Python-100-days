import requests, os
from datetime import datetime

USERNAME = "sdc331"
TOKEN = os.environ.get("TOKEN")
GRAPH = "cycle1"

pixela_endpoint = "https://pixe.la/v1"
pixela_graph_endpoint = f"{pixela_endpoint}/users/{USERNAME}/graphs"
today = datetime.now()


headers = {
    "X-USER-TOKEN": TOKEN
}

post_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "06.04",
}

put_pixel = {
    "quantity": "23.12",
}

# with requests.post(url=f"{pixela_graph_endpoint}/{GRAPH}", json=post_pixel, headers=headers) as req:
#     print(req.text)

with requests.put(url=f"{pixela_graph_endpoint}/{GRAPH}/{today.strftime('%Y%m%d')}", json=put_pixel, headers=headers) as req:
    print(req.text)