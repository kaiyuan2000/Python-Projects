TOKEN = "jjajksd8123a"
USERNAME = "kaiyuan12345"
GRAPH1_ID = "graph1"

import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN ,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH1_ID,
    "name" : "Gym Graph",
    "unit" : "commit",
    "type" : "int",
    "color" : "sora",
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

addpixel_endpoint = f"{graph_endpoint}/{GRAPH1_ID}"
addpixel_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : "1" ,
}

# response = requests.post(url=addpixel_endpoint, json=addpixel_params, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1_ID}/20230826"
update_params = {
    "quantity" : "5"
}

# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH1_ID}/20230826"

response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)