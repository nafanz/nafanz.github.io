import json
import socket
import requests
from urllib.parse import urlparse
from prettytable import PrettyTable
from requests.exceptions import SSLError, RequestException

session = requests.Session()
session.headers.update(
    {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache'
    }
)

sheet = PrettyTable()
sheet.field_names = [
    'url',
    'ip',
    'status_code'
]

sheet.align = 'l'

with open('spreadsheet.json') as file:
    spreadsheet = json.loads(file.read())

for item in spreadsheet:
    name = item['Name'].split("'")[1]

    try:
        # Получаем только hostname (mobisystems.com), scheme (https) и path (/en-us/mobidrive) нам не нужны
        name_to_ip = socket.gethostbyname(urlparse(name).hostname)
    except socket.gaierror as error:
        name_to_ip = None
        print(error)

    try:
        bucket = session.get(url=name)
        status = bucket.status_code
    except (SSLError, RequestException) as error:
        status = None
        print(error)

    sheet.add_row(
        [
            name,
            name_to_ip,
            status
        ]
    )

print(sheet)
