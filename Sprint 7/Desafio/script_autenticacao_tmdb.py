import requests
import pandas as pd

url = "https://api.themoviedb.org/3/account"

headers = {
    "accept": "application/json",
    "Authorization": ""
}

response = requests.get(url, headers=headers)

print(response.text)
