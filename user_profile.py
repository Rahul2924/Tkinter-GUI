import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Data entry from")

frame = tkinter.Frame(window)
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

first_name_label = tkinter.Label(user_info_frame,text="First Name")
first_name_label.grid(row=0,column=0)
last_name_label = tkinter.Label(user_info_frame,text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)


window.mainloop()
