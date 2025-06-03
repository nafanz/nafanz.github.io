import requests

spreadsheet = requests.get(url='https://nafanz.github.io/spreadsheet.json').json()

for item in spreadsheet:
    name = item['Name'].split("'")[1]
    print(name)
    bucket = requests.get(
        url=name,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
        }
    )

    match bucket.status_code:
        case 200:
            pass
        case _:
            print(bucket.url)
            print(bucket.status_code)
            print()
