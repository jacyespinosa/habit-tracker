import requests
from datetime import datetime as dt

USERNAME = "ENTER USERNAME"
TOKEN = "ENTER TOKEN"
GRAPH_ID = "ENTER OWN GRAPH ID"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_PARAMETERS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# pixela_response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMETERS)
# print(pixela_response.response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_CONFIG = {
    "id": GRAPH_ID,
    "name": "Book Reading Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CONFIG, headers=HEADERS)
# print(graph_response.text)

today = dt(year=2021, month=3, day=27)
print(today.strftime('%Y%m%d'))

POST_ENDPONT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
POST_CONFIG = {
    "date": today.strftime('%Y%m%d'),
    "quantity": "30",
}

post_response = requests.post(url=POST_ENDPONT, json=POST_CONFIG, headers=HEADERS)
print(post_response.text)
