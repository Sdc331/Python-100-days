import requests
from datetime import datetime

LAT = 52.498537
LNG = 13.380209
TODAY = str(datetime.now().date())
HOUR = datetime.now().hour
MINUTE = datetime.now().minute

### Setup response from ISS api to gather current lat/lng ###

current_iss = requests.get("http://api.open-notify.org/iss-now.json")
iss_lat = current_iss.json()['iss_position']['latitude']
iss_lat = float(iss_lat)
iss_lng = current_iss.json()['iss_position']['longitude']
iss_lng = float(iss_lng)

print(iss_lat, iss_lng)

### Setup api response from sunrise-sunset.org ###

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0,
}
sunrise_sunset = requests.get("https://api.sunrise-sunset.org/json", parameters)
sunrise_sunset.raise_for_status()

### Format api response into variables to extract minute/hour for sunrise and sunset respectivelly ###

sunrise = sunrise_sunset.json()['results']['sunrise']
sunrise = sunrise.split("T")
sunrise = sunrise[1].split(":")
sunrise_hour = int(sunrise[0])
sunrise_minute = int(sunrise[1])

sunset = sunrise_sunset.json()['results']['sunset']
sunset = sunset.split("T")
sunset = sunset[1].split(":")
sunset_hour = int(sunset[0])
sunset_minute = int(sunset[1])


### Check if the sun is set and if the current ISS position is CLOSE to set LNG and LAT constants. 

if HOUR <= sunrise_hour and MINUTE <= sunrise_minute or HOUR >= sunset_hour and MINUTE >= sunset_minute:
    if abs(LAT % iss_lat) <= 1 and abs(LNG % iss_lng) <= 1:
        print("ISS might be visible from your location")
