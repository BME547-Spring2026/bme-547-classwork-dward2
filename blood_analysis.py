def interface():
    keep_running = True
    while keep_running:
        print("My Program")
        print("Options:")
        print("1-HDL")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
    return
    
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
    
    
    
interface()

    