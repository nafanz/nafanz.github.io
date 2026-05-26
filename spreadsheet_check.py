import json
import socket
import requests
from urllib.parse import urlparse
from requests.exceptions import SSLError, RequestException

session = requests.Session()
session.headers.update(
    {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36',
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache'
    }
)

with open('spreadsheet.json') as file:
    spreadsheet = json.loads(file.read())

for item in spreadsheet:
    name = item['Name'].split("'")[1]
    print(name)

    try:
        # Получаем только hostname (mobisystems.com), scheme (https) и path (/en-us/mobidrive) нам не нужны
        name_to_ip = socket.gethostbyname(urlparse(name).hostname)
        print(name_to_ip)
    except socket.gaierror as error:
        print(error)

    try:
        bucket = session.get(url=name)
        print(bucket.url)
        print(bucket.status_code)
        print()
    except SSLError as ssl_error:
        print(ssl_error)
    except RequestException as request_exception:
        print(request_exception)
