import requests
import os
from datetime import datetime

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

now = datetime.now()
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

answer = input("Tell me what exercise you did : ")

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

params = {
    "query" : answer ,
    "gender" : "male",
    "weight_kg" : 80,
    "height_cm" : 175,
    "age" : 23,
}

response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
data = response.json()

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response1 = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, auth= (USERNAME,PASSWORD))
    print(response1.text)