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

def input_HDL_value():
    choice = input("Enter the HDL result: ")
    return choice
    
def check_HDL(hdl_input):
    hdl_value = int(hdl_input)
    if hdl_value >= 60:
        return "Normal"
    elif 40 <= hdl_value < 60:
        return "Borderline Low"
    elif hdl_value < 40:
        return "Low"
        
def output_HDL_result(hdl_result):
    print("The result of the HDL test is {}".format(hdl_result))
    return
    
def HDL_driver():
    hdl_input = input_HDL_value()
    hdl_result = check_HDL(hdl_input)
    output_HDL_result(hdl_result)
    
def input_LDL_value():
    choice = input("Enter the LDL result: ")
    return choice
    
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
        
def output_LDL_result(ldl_result):
    print("The result of the LDL test is {}".format(ldl_result))
    return
    
def LDL_driver():
    ldl_input = input_LDL_value()
    ldl_result = check_LDL(ldl_input)
    output_LDL_result(ldl_result)


interface()
