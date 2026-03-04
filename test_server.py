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