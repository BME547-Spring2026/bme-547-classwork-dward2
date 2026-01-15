def interface():
    keep_running = True
    while keep_running:
        print("My Program")
        print("Options:")
        print("1-HDL")
        print("2-LDL")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            generic_driver("HDL")
        elif choice == "2":
            generic_driver("LDL")
    return
    
def input_test_value(test_name):
    choice = input("Enter the {} result: ".format(test_name))
    return choice
    
def get_test_ranges(test_name):
    if test_name == "HDL":
        ranges = ((0, "Low"), (40, "Borderline Low"),(60, "Normal"))
    elif test_name == "LDL":
        ranges = ((0, "Normal"), (130, "Borderline High"), (160, "High"), (190, "Very High"))
    return ranges

def generic_test_analysis(test_ranges, test_result):
    test_value = int(test_result)
    for i in range(len(test_ranges)-1):
        if test_ranges[i][0] <= test_value < test_ranges[i+1][0]:
            return test_ranges[i][1]
    return test_ranges[-1][1]
        
def output_test_result(test_name, test_value, test_result):
    print("The result of {} for the {} test is {}".format(test_value, test_name, test_result))
    return
    
def generic_driver(test_name):
    test_input = input_test_value(test_name)
    test_ranges = get_test_ranges(test_name)
    test_result = generic_test_analysis(test_ranges, test_input)
    output_test_result(test_input, test_name, test_result)
        
interface()

    