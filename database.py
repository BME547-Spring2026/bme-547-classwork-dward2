"""

    patient = {"first name": <first_name>, "last name": <last_name>", "mrn": <mrn_int>, "age": <age_int>}
   
* Write create_patient that receives one input line (example: "Ann Ables, 123, 34\n") and 
  returns a patient dictionary
* Write another function that iterates through the input (patient_all) and calls create_patient for each patient 
  and prints patient dictionary

"""


def load_patient_file():
    # Example using open/close
    in_file = open("patient_data.txt", "r")
    patient_1 = in_file.readlines()
    print(patient_1)
    print(type(patient_1))
    patient_2 = in_file.readline()
    print(patient_2)
    in_file.close()

    # Example using with/open
    with open("patient_data.txt", "r") as in_file:
        patient_all = in_file.readlines()
    print(patient_all)

    return patient_all
    
def create_patient(line):
    line = line.strip("\n")
    data = line.split(",")
    first_name, last_name = data[0].split(" ")
    patient = {"first_name": first_name, "last_name": last_name,
               "mrn": int(data[1]), "age": int(data[2])}
    return patient


def process_all_patients(patient_raw_data):
    db = []
    for item in patient_raw_data:
        patient = create_patient(item)
        print(patient)
        db.append(patient)
    return db


def main():
    patient_raw_data = load_patient_file()
    db = process_all_patients(patient_raw_data)
    print(db)
    

if __name__ == "__main__":
    main()
