import pytest

from server import app
from database import db


client = app.test_client()


def test_post_add_patient():
    test_json = {"first_name": "fn",
                 "last_name": "ln",
                 "mrn": 1234,
                 "age": 35}
    r = client.post("/add_patient", json=test_json)
    assert r.text == "Successful addition"
    assert r.status_code == 200
    assert len(db) == 1


def test_post_add_patient_wrong_key():
    db.clear()
    test_json = {"fn": "fn",
                 "last_name": "ln",
                 "mrn": 1234,
                 "age": 35}
    r = client.post("/add_patient", json=test_json)
    assert r.status_code == 400
    assert len(db) == 0


@pytest.mark.parametrize("in_data, expected_keys, expected_types, expected", [
    ({"one": 1, "two": 2.3, "three": "str"},
     ["one", "two", "three"],
     [int, float, str],
     (True, 200)),
    ({"one": 1}, ["one", "two"], [int, float],
     ("Key two not found in input", 400)),
    ({"one": 1, "two": "2.2"}, ["one", "two"], [int, float],
     ("Key two has a value type of <class 'str'> "
      "but should be <class 'float'>", 400)),
    ([1, 2], ["one", "two"], [int, int],
     ("Input to route must be a dictionary", 400)),
    ({"one": 1, "two": 2.2}, ["one"], [int],
     (True, 200))

])
def test_validate_post_input(in_data, expected_keys,
                             expected_types, expected):
    from server import validate_post_input
    response = validate_post_input(in_data,
                                   expected_keys,
                                   expected_types)
    assert response[0] == expected[0]
    assert response[1] == expected[1]


def test_post_add_test_data():
    db.clear()
    patient_json = {"first_name": "fn",
                    "last_name": "ln",
                    "mrn": 1234,
                    "age": 35}
    r = client.post("/add_patient", json=patient_json)
    test_json = {"mrn": 1234,
                 "test_name": "HDL",
                 "test_value": 65.0}
    r = client.post("/add_test_data", json=test_json)
    assert r.text == "Successful addition"
    assert r.status_code == 200
    assert db[0].tests[0] == ("HDL", 65.0)


def test_post_add_test_data_fail_validation():
    db.clear()
    patient_json = {"first_name": "fn",
                    "last_name": "ln",
                    "mrn": 1234,
                    "age": 35}
    r = client.post("/add_patient", json=patient_json)
    test_json = {"mrn": 1234,
                 "testname": "HDL",
                 "test_value": 65.0}
    r = client.post("/add_test_data", json=test_json)
    assert r.text == "Key test_name not found in input"
    assert r.status_code == 400


def test_get_get_patient_info():
    db.clear()
    patient_json = {"first_name": "fn",
                    "last_name": "ln",
                    "mrn": 1234,
                    "age": 35}
    r = client.post("/add_patient", json=patient_json)
    test_json = {"mrn": 1234,
                 "test_name": "HDL",
                 "test_value": 65.0}
    r = client.post("/add_test_data", json=test_json)
    r = client.get("/get_patient_info/1234")
    assert r.text == ("Name: fn ln\n"
                      "  MRN: 1234\n"
                      "  Age: 35\n"
                      "  Tests: [('HDL', 65.0)]\n")
    assert r.status_code == 200


def test_get_get_patient_info_bad_mrn():
    r = client.get("/get_patient_info/mrn")
    assert r.text == ("/get_patient_info/<mrn> expects an integer"
                      "for the mrn value")
    assert r.status_code == 400


def test_get_get_patient_info_no_patient():
    db.clear()
    r = client.get("/get_patient_info/11")
    assert r.text == "MRN 11 not found"
    assert r.status_code == 400
