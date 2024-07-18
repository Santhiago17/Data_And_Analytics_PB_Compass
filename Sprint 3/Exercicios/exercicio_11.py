import json

file_path = 'person.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
    
print(data)