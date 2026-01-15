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
        
        
interface()
