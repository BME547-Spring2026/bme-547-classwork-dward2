import pytest
from pymongo import MongoClient
uri = "mongodb+srv://db_sp26:db_sp26@bme547.ba348." \
              "mongodb.net/?appName=BME547"

client = MongoClient(uri)
client.admin.command({'ping': 1})
database = client["patient_db"]
collection = database["patient"]


def test_Patient_init():
    from database import Patient
    mrn = 123
    answer = Patient("fn", "ln", mrn, 33)
    assert answer.mrn == mrn


def test_Patient_is_minor():
    from database import Patient
    patient = Patient("fn", "ln", 123, 5)
    answer = patient.is_minor()
    assert answer is True


def test_Patient_add_test():
    from database import Patient
    patient = Patient("fn", "ln", 123, 5)
    patient.add_test("HDL", 50)
    assert patient.tests == [("HDL", 50)]


def test_Patient_save():
    from database import Patient
    Patient.make_connection()
    patient = Patient("fn", "ln", 123, 50)
    patient.save()
    answer = collection.find_one({"_id": 123})
    answer = Patient.retrieve_by_mrn(123)
    assert answer["first_name"] == "fn"


def test_create_patient():
    from database import create_patient, Patient
    input_data = "David Ward, 12345, 57\n"
    expected = Patient("David",
                       "Ward",
                       12345,
                       57,
                       )
    answer = create_patient(input_data)
    assert isinstance(answer, Patient)
    assert answer.first_name == "David"
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
    assert answer is None


"""
def test_add_test_data():
    from database import add_test_data, db, \
        load_patient_file, process_all_patients
    # Arrange
    patient = {"mrn": 12345, "tests": []}
    db.append(patient)
    # Act
    add_test_data()
    answer = len(db[0]["tests"])
    #Cleanup
    db.clear()
    # Assert
    assert answer == 1
 """
