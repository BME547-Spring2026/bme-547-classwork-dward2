import requests

server = 'http://127.0.0.1:5000'

r = requests.get(server + "/")
print(r.status_code)
print(r.text)

out_json = {"name": "Ann Ables",
            "test_value": 60
            }
r = requests.post(server+"/hdl_analysis", json=out_json)
print(r.status_code)
print(r.text)
if r.status_code != 200:
    answer = r.text
else:
    answer = r.json()
print(type(answer))
print(answer)

r = requests.get(server+"/hdl_analysis/35")
print(r.status_code)

patient_json = {"first_name": "Ann",
                "last_name": "Ables",
                "mrn": 23423,
                "age": 35}
r = requests.post(server + "/add_patient",
                  json=patient_json)
print(r.status_code)
print(r.text)

test_json = {"mrn": 23423,
             "test_name": "HDL",
             "test_value": 50.0}
r = requests.post(server + "/add_test_data",
                  json=test_json)
print(r.status_code)
print(r.text)