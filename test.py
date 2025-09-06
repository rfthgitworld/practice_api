import requests
import pprint

url = "https://sandbox.zestfuldata.com/parseIngredients"


payload = {}
headers = {
	"Content-Type": "application/json"
}
data = {
    "ingredients": ["bacon"]
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())

# pprint.pprint(response.json())