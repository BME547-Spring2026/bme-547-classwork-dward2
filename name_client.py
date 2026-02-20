"""
Code to demonstrate a POST request to the name server.
"""

import requests

out_json = {
   "name": "David Ward",
   "net_id": "daw74",
   "e-mail": "david.a.ward@duke.edu"
}
r = requests.post("http://vcm-51170.vm.duke.edu:5000/student", json=out_json)

print(r.status_code)
print(r.text)

r = requests.get("http://vcm-51170.vm.duke.edu:5000/list")
print(r.text)
