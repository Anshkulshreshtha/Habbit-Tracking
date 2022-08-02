import requests
from datetime import datetime

TOKEN = "asdfg0mddjbzkl"
USERNAME = "ynsh"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "Yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)



graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)



pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime(year=2022, month=6, day=23)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many kilometer's you run today ?")
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# put request

update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

new_pixel_config = {
    "quantity": "98.5",
}

# response = requests.put(url=update_endpoint, json=new_pixel_config, headers=headers)
# print(response.text)

# delete requests

delete_endpoint = f"{update_endpoint}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)