import tkinter as tk
from tkinter import ttk
import database


base_font = ("arial", 24)


def main_window():

    def cancel_btn_cmd():
        root.destroy()

    def ok_btn_cmd():
        # Get data from GUI
        patient_name = name_value.get()
        patient_id = id_value.get()
        patient_blood_letter = blood_letter_value.get()
        patient_rh = rh_value.get()
        patient_dc = dc_value.get()
        # Call other functions to do work
        answer = database.create_patient_from_gui(patient_name, patient_id)
        # Update GUI with any response
        label_status.config(text=answer)
        print(patient_name)
        print(patient_id)
        print("{}{}".format(patient_blood_letter, patient_rh))
        print(patient_dc)
        clear_gui()

    def clear_gui():
        name_value.set("")
        id_value.set("")
        blood_letter_value.set(" ")
        rh_value.set("+")
        dc_value.set("")

    def check_entry_box():
        if name_value.get() != "":
            button_ok.config(state=tk.NORMAL)
        else:
            button_ok.config(state=tk.DISABLED)

    root = tk.Tk()
    # root.geometry("800x600")
    root.title("Blood Donor Database")

    title_label = tk.Label(root, text="Blood Donor Database",
                           font=base_font)
    title_label.grid(column=0, row=0, columnspan=2, sticky=tk.W)
    name_label = tk.Label(root, text="Name:", font=base_font)
    name_label.grid(column=0, row=1, sticky=tk.E, padx=5)

    name_value = tk.StringVar()
    # name_value.set("Enter your name here")
    entry_name = tk.Entry(root, font=base_font, textvariable=name_value)
    entry_name.grid(column=1, row=1)
    
    id_value = tk.StringVar()
    label_id = tk.Label(root, text="Id:", font=base_font)
    label_id.grid(column=0, row=2, sticky=tk.E, padx=5)
    entry_id = tk.Entry(root, font=base_font, textvariable=id_value)
    entry_id.grid(column=1, row=2)

    blood_letter_value = tk.StringVar()
    blood_letter_value.set(" ")
    radio_a = tk.Radiobutton(root, text="A", font=base_font,
                             variable=blood_letter_value,
                             value="A")
    radio_a.grid(column=0, row=3, sticky=tk.W, padx=5)
    radio_b = tk.Radiobutton(root, text="B", font=base_font,
                             variable=blood_letter_value,
                             value="B")
    radio_b.grid(column=0, row=4, sticky=tk.W, padx=5)
    radio_ab = tk.Radiobutton(root, text="AB", font=base_font,
                             variable=blood_letter_value,
                             value="AB")
    radio_ab.grid(column=0, row=5, sticky=tk.W, padx=5)
    radio_o = tk.Radiobutton(root, text="O", font=base_font,
                             variable=blood_letter_value,
                             value="O")
    radio_o.grid(column=0, row=6, sticky=tk.W, padx=5)

    rh_value = tk.StringVar()
    rh_value.set("+")
    check_rh = tk.Checkbutton(root, text="rH Positive", font=base_font,
                              variable=rh_value, onvalue="+", offvalue="-")
    check_rh.grid(column=1, row=4)

    button_ok = tk.Button(root, text="Ok", font=base_font,
                          command=ok_btn_cmd,
                        #   state=tk.DISABLED
                          )
    button_ok.grid(column=1, row=6, sticky=tk.NSEW)
    button_cancel = tk.Button(root, text="Cancel", font=base_font,
                              command=cancel_btn_cmd)
    button_cancel.grid(column=2, row=6)

    label_dc = tk.Label(root, text="Nearest Donation Center", font=base_font)
    label_dc.grid(column=2, row=0)

    dc_value = tk.StringVar()
    combobox_dc = ttk.Combobox(root, font=base_font, textvariable=dc_value)
    combobox_dc["values"] = ["Durham", "Raleigh", "Cary", "Apex"]
    combobox_dc.state(['readonly'])
    combobox_dc.grid(column=2, row=1)

    label_status = tk.Label(root, text="")
    label_status.grid(column=2, row=4)


    root.mainloop()
    print("Finished")

if __name__ == "__main__":
    main_window()
