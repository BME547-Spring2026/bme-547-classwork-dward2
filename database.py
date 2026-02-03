"""

    patient = {"first name": <first_name>, "last name": <last_name>", "mrn": <mrn_int>, "age": <age_int>,
               "tests": [("HDL", 65), ("LDL", 40)]}
   
* Write create_patient that receives one input line (example: "Ann Ables, 123, 34\n") and 
  returns a patient dictionary
* Write another function that iterates through the input (patient_all) and calls create_patient for each patient 
  and prints patient dictionary

"""


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
    patient = {"first_name": first_name, "last_name": last_name,
               "mrn": int(data[1]), "age": int(data[2]),
               "tests": []}
    return patient


def process_all_patients(patient_raw_data):
    db = []
    for item in patient_raw_data:
        patient = create_patient(item)
        print(patient)
        db.append(patient)
    return db
    
    
def find_patient(db, mrn):
    for patient in db:
        if patient["mrn"] == mrn:
            return patient
    return None
    
    
def add_test_data(db):
    # REad in the blood_test_data file
    test_data_raw = load_patient_file("blood_test_data.txt")
    # For each line in the file,
    for item in test_data_raw:
        line = item.strip("\n")
        mrn, test_name, test_value = line.split(",")
        mrn = int(mrn)
        # Find the correct patient in the db
        patient = find_patient(db, mrn)
        # Add the test to that patient record
        patient["tests"].append((test_name, float(test_value)))
    return db
    

def is_minor(patient):
    if patient["age"] < 18:
        return True
    else:
        return False
        

def output_patient(patient):
    print("Name: {} {}".format(patient["first_name"], 
                               patient["last_name"]))
    print("  MRN: {}".format(patient["mrn"]))
    print("  Age: {}".format(patient["age"]))


def print_database(db):
    for patient in db:
        output_patient(patient)

def main():
    patient_raw_data = load_patient_file("patient_data.txt")
    db = process_all_patients(patient_raw_data)
    print_database(db)
    db = add_test_data(db)
    print_database(db)
    

if __name__ == "__main__":
    main()
