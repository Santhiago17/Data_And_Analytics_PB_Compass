import requests
import pandas as pd

url = "https://api.themoviedb.org/3/account"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3OWYwNjI3YWNlMjI1NGE0NTM0MTcxN2U3Nzg0MTc1YSIsIm5iZiI6MTcyNjUwNzY4OS40MTAxOSwic3ViIjoiNjZlODY4N2JkN2JjY2E1MjRkYjEyZTY5Iiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.Nc3M1C__qCzMZG4FyBJYlmMPbEYnkdcr48F_baakbhQ"
}

response = requests.get(url, headers=headers)

print(response.text)
