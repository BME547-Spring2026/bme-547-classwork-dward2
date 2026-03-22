import tkinter as tk

base_font = ("arial", 24)

def main_window():
    root = tk.Tk()
    # root.geometry("800x600")
    root.title("Blood Donor Database")

    title_label = tk.Label(root, text="Blood Donor Database",
                           font=base_font)
    title_label.grid(column=0, row=0)
    name_label = tk.Label(root, text="Name:", font=base_font)
    name_label.grid(column=0, row=1)

    entry_name = tk.Entry(root, font=base_font)
    entry_name.grid(column=1, row=1)
    
    label_id = tk.Label(root, text="Id:", font=base_font)
    label_id.grid(column=0, row=2)
    entry_id = tk.Entry(root, font=base_font)
    entry_id.grid(column=1, row=2)

    radio_a = tk.Radiobutton(root, text="A", font=base_font)
    radio_a.grid(column=0, row=3)
    radio_b = tk.Radiobutton(root, text="B", font=base_font)
    radio_b.grid(column=0, row=4)
    radio_ab = tk.Radiobutton(root, text="AB", font=base_font)
    radio_ab.grid(column=0, row=5)
    radio_o = tk.Radiobutton(root, text="O", font=base_font)
    radio_o.grid(column=0, row=6)

    check_rh = tk.Checkbutton(root, text="rH Positive", font=base_font)
    check_rh.grid(column=1, row=4)

    button_ok = tk.Button(root, text="Ok", font=base_font)
    button_ok.grid(column=1, row=6)
    button_cancel = tk.Button(root, text="Cancel", font=base_font)
    button_cancel.grid(column=2, row=6)

    root.mainloop()
    print("Finished")

if __name__ == "__main__":
    main_window()
