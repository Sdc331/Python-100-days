import requests, os, json
from datetime import datetime


KEY = os.environ.get("NUTR_KEY")
APP_ID = os.environ.get("NUTR_ID")
API_URL = "https://trackapi.nutritionix.com"
EXE_ENDPOINT = "/v2/natural/exercise"
USER_ID = os.environ.get("USER_ID")
SHEETY_URL = f"https://api.sheety.co/{USER_ID}/myWorkouts/workouts"

today = str(datetime.now().strftime("%d-%m-%Y"))
time = str(datetime.now().time().strftime("%H:%M"))

headers_nutr = {
    "x-app-id": APP_ID,
    "x-app-key": KEY,
}

headers = {
    "Content-Type": "application/json",
}


parameters = {
    "query": input("Provide what exercises you've done: "),
}
with requests.post(url=f"{API_URL}{EXE_ENDPOINT}", data=parameters, headers=headers_nutr) as req:
    data = req.json()

for each in data["exercises"]:
    options = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": each['name'],
            "duration": each['duration_min'],
            "calories": each['nf_calories'],
        },
    }
    options = json.dumps(options)
    final = json.loads(options)
    print(f"Type of options: {type(options)}\nOutput:{options}")
    print(f"Type of final: {type(final)}\nOutput:{final}")
    with requests.post(url=SHEETY_URL, json=final, headers=headers) as req:
        req.raise_for_status()
        print(req.text)
