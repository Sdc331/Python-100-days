import requests
from datetime import datetime

LAT = 52.498537
LNG = 13.380209
TODAY = str(datetime.now().date())
HOUR = datetime.now().hour
MINUTE = datetime.now().minute

### Setup response from ISS api to gather current lat/lng ###

current_iss = requests.get("http://api.open-notify.org/iss-now.json")
data = current_iss.json()
iss_lat = float(data['iss_position']['latitude'])
iss_lng = float(data['iss_position']['longitude'])


### Setup api response from sunrise-sunset.org ###

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0,
}
sunrise_sunset = requests.get("https://api.sunrise-sunset.org/json", parameters)
sunrise_sunset.raise_for_status()
sun_data = sunrise_sunset.json()
### Format api response into variables to extract minute/hour for sunrise and sunset respectivelly ###

sunrise_hour = int(sun_data['results']['sunrise'].split("T")[1].split(":")[0])
sunrise_minute = int(sun_data['results']['sunrise'].split("T")[1].split(":")[1])

sunset_hour = int(sun_data['results']['sunset'].split("T")[1].split(":")[0])
sunset_minute = int(sun_data['results']['sunset'].split("T")[1].split(":")[1])

### Check if the sun is set and if the current ISS position is CLOSE to set LNG and LAT constants. 

if HOUR <= sunrise_hour and MINUTE <= sunrise_minute or HOUR >= sunset_hour and MINUTE >= sunset_minute:
    if LAT % iss_lat <= 1 and LNG % iss_lng <= 1:
        print("ISS might be visible from your location")
    else:
        print("Keep looking")
