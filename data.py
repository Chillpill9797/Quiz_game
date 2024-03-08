import requests
AMOUNT = 10
DIFFICULTY = "medium"
TYPE = "boolean"

parameters = {
    "amount": AMOUNT,
    "difficulty": DIFFICULTY,
    "type": TYPE,
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

