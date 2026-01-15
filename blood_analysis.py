def interface():
    keep_running = True
    while keep_running:
        print("My Program")
        print("Options:")
        print("9-Quit")
        choice = input("Enter your choice: ")
        if choice == "9":
            keep_running = False
    return
    
interface()

    