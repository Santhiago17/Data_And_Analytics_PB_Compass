import requests

api_key = ""

url = "https://api.themoviedb.org/3/genre/movie/list"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer "
}

response = requests.get(url, headers=headers)
generos = response.json().get('genres', [])
print(generos)