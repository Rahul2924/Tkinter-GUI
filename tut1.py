from tkinter import *
root = Tk()
root.geometry("655x333")

f1 = Frame(root, bg="grey", borderwidth=6, relief = SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, bg="blue",borderwidth=7, relief= SUNKEN)
f2.pack(side=TOP, fill="x")

f3 = Frame(root, bg="white")
f3.pack(side=BOTTOM, padx=500)

b1 = Button(f3, fg="yellow" , text="Print now")
b1.pack()

l= Label(f1, text="MY FIRST PROJECT")
l.pack( pady=142)

l= Label(f2, text= "PORTFOLIO")
l.pack()



root.mainloop()