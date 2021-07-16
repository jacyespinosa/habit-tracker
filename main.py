import requests


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

pixela_response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMETERS)
print(pixela_response.response.text)

