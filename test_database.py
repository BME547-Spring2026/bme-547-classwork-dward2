import pytest


def test_create_patient():
    from database import create_patient
    input_data = "David Ward, 12345, 57\n"
    expected = {"first_name": "David",
                "last_name": "Ward",
                "mrn": 12345,
                "age": 57,
                "tests": []}
    answer = create_patient(input_data)
    assert answer == expected