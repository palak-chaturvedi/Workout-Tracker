import requests as requests
import datetime
import os
PASSWORD = YOUR_PASSWORD
USERNAME = YOUR_USERNAME
AUTH = (USERNAME,PASSWORD)
GENDER = "male"
Weight_kg = 75
height_cm = 172
AGE = 19
APP_ID = YOUR_APPID #from  Nutritionix "Natural Language for Exercise" API Documentation,
NUTRITION_API =  YOUR_GENERATED_API
os.environ['SKEETY_USER']=USERNAME
os.environ['SKEETY_PASS']=PASSWORD
os.environ['APP_ID']=APP_ID
os.environ['APP_API']=NUTRITION_API
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
skeety_api = "https://api.sheety.co/4623e8db5edfc3793cc653892bb0e74e/workoutApp/workouts"

ex_text = input("What did you do today:")
ex_params = {
    "query": ex_text,
    "gender":GENDER,
    "weight_kg":Weight_kg,
    "height_cm":height_cm,
    "age":AGE,
}

headers = {
    "x-app-id":APP_ID,
    "x-app-key":NUTRITION_API,
}


response1 = requests.post(url=exercise_endpoint, json=ex_params, headers=headers)
response = response1.json()
date = datetime.datetime.now()
date2 = date.strftime("%d/%m/%Y")
time = date.strftime("%H:%M:%S")
# print(time)
for exercise in response["exercises"]:
    skeety_params = {
        "workout":{
            "date": date2,
            "time": time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"],
        }
    }
    result = requests.post(url=skeety_api, json=skeety_params , auth=AUTH)
    # print(result.text)
# print(response.json())
