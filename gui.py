import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import database
from PIL import Image, ImageT

base_font = ("arial", 24)

def load_tk_image(filename):
    pillow_image = Image.open(filename)
    width, height = pillow_image.size
    if width > height:
        alpha = 100/width
    else:
        alpha = 100/height
    new_width = round(width*alpha)
    new_height = round(height*alpha)
    pillow_image = pillow_image.resize((new_width, new_height))
    tk_image = ImageTk.PhotoImage(pillow_image)
    return tk_image


def main_window():

    def cancel_btn_cmd():
        """ Closes window when cancel button is clicked

        This subfunction is linked to the cancel button.  When the button is clicked,
        this function uses the destroy method of the root window that causes it to close
        and terminates the mainloop.
        
        """
        root.destroy()

    def ok_btn_cmd():
        # Get data from GUI
        choice = messagebox.askyesno("Save Patient", "Do you want to save this patient")
        print(choice)
        if choice is False:
            return
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
        root.after(2000, change_title_color)

    def clear_gui():
        name_value.set("")
        id_value.set("")
        blood_letter_value.set(" ")
        rh_value.set("+")
        dc_value.set("")

    def check_entry_box(x):
        if name_value.get() != "":
            button_ok.config(state=tk.NORMAL)
        else:
            button_ok.config(state=tk.DISABLED)

    def change_title_color():
        title_color = title_label.cget("foreground")
        if title_color == "red":
            new_color = "black"
        else:
            new_color = "red"
        title_label.configure(foreground=new_color)
        root.after(2000, change_title_color)

    def load_img_cmd():
        filename = filedialog.askopenfilename()
        if filename == "":
            return
        new_image = load_tk_image(filename)
        label_image.configure(image=new_image)
        label_image.image = new_image

    root = tk.Tk()
    # root.geometry("800x600")
    root.title("Blood Donor Database")

    title_label = tk.Label(
                           root, text="Blood Donor Database",
                           font=base_font,
                           foreground="red",
                           )
    title_label.grid(column=0, row=0, columnspan=2, sticky=tk.W)
    name_label = tk.Label(root, text="Name:", font=base_font)
    name_label.grid(column=0, row=1, sticky=tk.E, padx=5)

    name_value = tk.StringVar()
    # name_value.set("Enter your name here")
    entry_name = tk.Entry(root, font=base_font, textvariable=name_value)
    entry_name.grid(column=1, row=1)
    entry_name.bind("<KeyPress>", check_entry_box)
    
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
                           state=tk.DISABLED
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

    image_title = tk.Label(root, text="Patient Image", font=base_font)
    image_title.grid(column=4, row=0)
    tk_image = load_tk_image("blank.png")
    label_image = tk.Label(root, image=tk_image)
    label_image.image = tk_image
    label_image.grid(column=4, row=1, rowspan=3)

    button_image = tk.Button(root, text="Load image", command=load_img_cmd,
                             font=base_font)
    button_image.grid(column=4, row=6)

    # root.after(2000, change_title_color)
    root.mainloop()
    print("Finished")

if __name__ == "__main__":
    main_window()
