def interface():
    print("Blood Analysis Program")
    keep_running = True
    while keep_running:
        print("Options:")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False

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
    
interface()
