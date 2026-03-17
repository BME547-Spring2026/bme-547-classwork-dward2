"""

    patient = {"first name": <first_name>, "last name": <last_name>",
               "mrn": <mrn_int>, "age": <age_int>,
               "tests": [("HDL", 65), ("LDL", 40)]}

* Write create_patient that receives one input line
  (example: "Ann Ables, 123, 34\n") and returns a patient dictionary
* Write another function that iterates through the input (patient_all)
  and calls create_patient for each patient and prints patient dictionary

"""
from pymongo import MongoClient

db = []


class Patient:

    client = None
    database = None
    collection = None

    @classmethod
    def make_connection(cls):
        uri = "mongodb+srv://db_sp26:db_sp26@bme547.ba348.mongodb.net/?appName=BME547"

        cls.client = MongoClient(uri)
        cls.client.admin.command({'ping': 1})
        cls.database = cls.client["patient_db"]
        cls.collection = cls.database["patient"]  

    def __init__(self, first_name, last_name, mrn,
                 age):
        self.first_name = first_name
        self.last_name = last_name
        self.mrn = mrn
        self.age = age
        self.tests = []

    def save(self):
        existing = self.collection.find_one({"_id": self.mrn})
        out_dict = self.output_dictionary()
        if existing is None:
            r = self.collection.insert_one(out_dict)
        else:
            r = self.collection.replace_one({"_id": self.mrn}, out_dict)
        return r
    
    @classmethod
    def retrieve_by_mrn(cls, mrn):
        new_dict = cls.collection.find_one({"_id": mrn})
        new_patient = Patient(new_dict["first_name"],
                              new_dict["last_name"],
                              new_dict["_id"],
                              new_dict["age"])
        new_patient.tests = new_dict["tests"]
        return new_patient
    
    def delete(self):
        self.collection.delete_one({"_id": self.mrn})

    def __repr__(self):
        return "Patient, mrn={}".format(self.mrn)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        if self.first_name != other.first_name:
            return False
        if self.last_name != other.last_name:
            return False
        if self.mrn != other.mrn:
            return False
        if self.age != other.age:
            return False
        if self.tests != other.tests:
            return False
        return True

    def output_patient(self):
        print("Name: {} {}".format(self.first_name,
                                   self.last_name))
        print("  MRN: {}".format(self.mrn))
        print("  Age: {}".format(self.age))
        print("  Tests:  {}".format(self.tests))

    def output_string(self):
        out_string = "Name: {} {}\n".format(self.first_name,
                                            self.last_name)
        out_string += "  MRN: {}\n".format(self.mrn)
        out_string += "  Age: {}\n".format(self.age)
        out_string += "  Tests: {}\n".format(self.tests)
        return out_string

    def is_minor(self):
        if self.age < 18:
            return True
        else:
            return False

    def add_test(self, test_name, test_value):
        self.tests.append((test_name, test_value))

    def output_dictionary(self):
        out_dict = {"first_name": self.first_name,
                    "last_name": self.last_name,
                    "_id": self.mrn,
                    "age": self.age,
                    "tests": self.tests}
        return out_dict


def load_patient_file(filename):
    # Example using open/close
    in_file = open(filename, "r")
    patient_all = in_file.readlines()
    # print(patient_1)
    # print(type(patient_1))
    # patient_2 = in_file.readline()
    # print(patient_2)
    in_file.close()

    # Example using with/open
    # with open("patient_data.txt", "r") as in_file:
    #     patient_all = in_file.readlines()
    print(patient_all)

    return patient_all


def create_patient(line):
    line = line.strip("\n")
    data = line.split(",")
    first_name, last_name = data[0].split(" ")
    patient = Patient(first_name, last_name,
                      int(data[1]),
                      int(data[2]))
    return patient


def add_single_patient(in_data):
    out_line = "{} {},{},{}".format(in_data["first_name"],
                                    in_data["last_name"],
                                    in_data["mrn"],
                                    in_data["age"])
    patient = create_patient(out_line)
    db.append(patient)


def process_all_patients(patient_raw_data):

    for item in patient_raw_data:
        patient = create_patient(item)
        print(patient)
        db.append(patient)


def find_patient(mrn):
    for patient in db:
        if patient.mrn == mrn:
            return patient
    return None


def add_test_data():
    # REad in the blood_test_data file
    test_data_raw = load_patient_file("blood_test_data.txt")
    # For each line in the file,
    for item in test_data_raw:
        line = item.strip("\n")
        mrn, test_name, test_value = line.split(",")
        mrn = int(mrn)
        add_test_data_to_db(mrn, test_name, test_value)


def add_test_data_to_db(mrn, test_name, test_value):
    # Find the correct patient in the db
    patient = find_patient(mrn)
    # Add the test to that patient record
    patient.add_test(test_name, float(test_value))


def print_database():
    for patient in db:
        patient.output_patient()


def get_patient_output(mrn):
    patient = find_patient(mrn)
    if patient is None:
        return None
    else:
        return patient.output_string()


def main():
    patient_raw_data = load_patient_file("patient_data.txt")
    process_all_patients(patient_raw_data)
    print_database()
    add_test_data()
    print_database()


def crud_tests():
    Patient.make_connection()
    # patient_1 = Patient("Ann", "Ables", 123, 30)
    # print(patient_1.save())

    new_patient = Patient.retrieve_by_mrn(123)
    new_patient.output_patient()
    new_patient.tests.append(("HDL", 50))
    new_patient.save()
    new_patient.output_patient()
    new_patient.delete()



if __name__ == "__main__":
    crud_tests()
