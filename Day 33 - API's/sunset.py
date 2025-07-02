import requests
from datetime import datetime

LAT = 52.498537
LNG = 13.380209
TODAY = str(datetime.now().date())
HOUR = datetime.now().hour

current_iss = requests.get("http://api.open-notify.org/iss-now.json")
iss_lat = current_iss.json()['iss_position']['latitude']
iss_lat = float(iss_lat)
iss_lng = current_iss.json()['iss_position']['longitude']
iss_lng = float(iss_lng)

print(iss_lat, iss_lng)

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0,
}
sunrise_sunset = requests.get("https://api.sunrise-sunset.org/json", parameters)
sunrise_sunset.raise_for_status()

sunrise = sunrise_sunset.json()['results']['sunrise']
sunrise = sunrise.split("T")
sunrise = sunrise[1].split(":")
sunrise_hour = int(sunrise[0])

sunset = sunrise_sunset.json()['results']['sunset']
sunset = sunset.split("T")
sunset = sunset[1].split(":")
sunset_hour = int(sunset[0])

if HOUR > sunset_hour or HOUR < sunrise_hour:
    if LAT % iss_lat < 100 and LNG % iss_lng < 100:
        print("CHECK")
