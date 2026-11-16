import json
import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url, timeout=10)
response.raise_for_status()
print(json.dumps(response.json(), indent=2))