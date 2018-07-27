#!/usr/bin/env python3

import requests
import json
 
print("Content-type: text/html")
print()
print("<h1>Hello world!</h1>")

r = requests.get("https://api.github.com/repos/nafanz/nafanz.github.io")
        
repos = r.json()

test
repos['updated_at']
print(repos['updated_at'])