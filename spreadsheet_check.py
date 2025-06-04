import json
import requests

with open('spreadsheet.json') as file:
    spreadsheet = json.loads(file.read())

for item in spreadsheet:
    name = item['Name'].split("'")[1]
    print(name)
    bucket = requests.get(
        url=name,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
        }
    )

    print(bucket.url)
    print(bucket.status_code)
    print()
