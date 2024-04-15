import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os


API_KEY = os.environ["API_KEY"]
APP_ID = os.environ['APP_ID']
USER = input("Enter username: ")
PASSWD = input("Enter your password: ")

api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_api = os.environ["SHEET_API"]
api_param = {
    "query": input("What exercise did you do?: "),
}
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

real_date = datetime.now()
date = real_date.strftime("%d/%m/%Y")
time = real_date.strftime("%H:%M:%S")

response = requests.post(url=api_endpoint, json=api_param, headers=headers)

data = response.json()
real_data = data["exercises"]
for exercise in real_data:
    basic = HTTPBasicAuth(username=USER, password=PASSWD)
    sheet_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    result = requests.post(url=sheet_api, json=sheet_params, auth=basic)
    print(result.text)
