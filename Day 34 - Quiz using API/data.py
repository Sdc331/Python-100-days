import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}
output = requests.get("https://opentdb.com/api.php", parameters)
output.raise_for_status()
data = output.json()
question_data = data["results"]
