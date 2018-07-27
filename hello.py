import requests
import json

r = requests.get("https://api.github.com/repos/nafanz/nafanz.github.io)

commits = r.json()

for item in commits:
print(item['author'])
print()