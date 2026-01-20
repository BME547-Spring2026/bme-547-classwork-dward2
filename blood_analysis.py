def interface():
    print("Blood Analysis Program")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()

def input_test_value(test_name):
    choice = input("Enter the {} result: ".format(test_name))
    return choice

def output_test_result(test_name, test_value, test_result):
    print("The result of {} for the {} test is {}".format(test_value, test_name, test_result))
    return
    
def check_HDL(hdl_input):
    hdl_value = int(hdl_input)
    if hdl_value >= 60:
        return "Normal"
    elif 40 <= hdl_value < 60:
        return "Borderline Low"
    elif hdl_value < 40:
        return "Low"
        
def HDL_driver():
    test_name = "HDL"
    test_input = input_test_value(test_name)
    test_result = check_HDL(test_input)
    output_test_result(test_input, test_name, test_result)
        
def check_LDL(ldl_input):
    ldl_value = int(ldl_input)
    if ldl_value < 130:
        return "Normal"
    elif 130 <= ldl_value < 160:
        return "Borderline High"
    elif 160 <= ldl_value < 190:
        return "High"
    elif ldl_value >= 190:
        return "Very High"
        
def LDL_driver():
    test_name = "LDL"
    test_input = input_test_value(test_name)
    test_result = check_LDL(test_input)
    output_test_result(test_input, test_name, test_result)

interface()
