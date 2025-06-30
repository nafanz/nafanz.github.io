import json
import socket
import requests

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'

with open('spreadsheet.json') as file:
    spreadsheet = json.loads(file.read())

for item in spreadsheet:
    name = item['Name'].split("'")[1]
    print(name)

    try:
        name_to_ip = socket.gethostbyname(name.split("//")[1])
        print(name_to_ip)
    except socket.gaierror as error:
        print(error)

    bucket = requests.get(
        url=name,
        headers={'User-Agent': user_agent}
    )

    print(bucket.url)
    print(bucket.status_code)
    print()
