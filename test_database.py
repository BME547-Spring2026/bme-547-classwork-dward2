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
    
    
def test_find_patient():
    from database import find_patient, create_patient, db
    # Arrange
    patient = create_patient("David Ward, 12345, 57\n")
    db.append(patient)
    # Act
    answer = find_patient(12345)
    # Assert
    assert answer == patient
    # Clean up
    db.clear()
    
    
def test_process_all_patients():
    from database import process_all_patients, db
    # Arrange
    input_data = ["David Ward, 12345, 57\n",
                  "Ann Ables, 23456, 30\n"]
    # Act
    process_all_patients(input_data)
    answer = len(db)
    # Cleanup
    db.clear()
    # Assert
    assert answer == 2
    
    
def test_find_patient_none():
    from database import find_patient
    # Act
    answer = find_patient(12345)
    # Assert
    assert answer == None
    

def test_add_test_data():
    

    