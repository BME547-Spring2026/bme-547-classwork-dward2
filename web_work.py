"""
Code to demonstrate a GET request to GitHub
"""

import requests

server = "https://api.github.com"

url = server+"/repos/dward2/bme547/branches"

r = requests.get(url)

print(type(r))
print(r)
print(r.status_code)
print(r.text)

answer = r.json()
print(type(answer))
if r.status_code == 200:
    for branch in answer:
        print(branch["name"])
