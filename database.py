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

    return


def main():
    load_patient_file()


if __name__ == "__main__":
    main()
