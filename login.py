import tkinter 


window = tkinter.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')  

frame = tkinter.Frame(bg="#333333")

login_label = tkinter.Label(frame,text = "login", bg='#333333',fg='#FF3399',font=("Arial",30))
username_label = tkinter.Label(frame,text = "username", bg='#333333',fg='#FF3399',font=("Arial",16))
username_entry = tkinter.Entry(frame,)
password_entry = tkinter.Entry(frame, show='*')
password_label = tkinter.Label(frame,text = "Password", bg='#333333',fg='#FF3399',font=("Arial",16))
login_button = tkinter.Button(frame, text='login')



login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0,padx=20)
username_entry.grid(row=1, column=1, pady=20,padx=20)
password_label.grid(row=2, column=0,padx=20)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)


frame.pack()

window.mainloop()