from tkinter import *

def click(event):
    text = event.widget.cget("text")
    print("text")
    
root = Tk()
root.geometry("644x900")
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue, font= "lucida 40 bold")
screen.pack(fill=X, ipadx= 8, padx=10, pady=10)

f= Frame(root, bg= "grey")
b= Button(f,text="9",padx=28, pady=22, font="lucida 19 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b= Button(f,text="8",padx=28, pady=22, font="lucida 19 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b= Button(f,text="7",padx=28, pady=22, font="lucida 19 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)


f.pack()

f= Frame(root, bg= "grey")
b= Button(f,text="6",padx=28, pady=22, font="lucida 19 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b= Button(f,text="5",padx=28, pady=22, font="lucida 19 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b= Button(f,text="4",padx=28, pady=22, font="lucida 19 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack()

f= Frame(root, bg= "grey")
b= Button(f,text="3",padx=28, pady=22, font="lucida 19 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b= Button(f,text="2",padx=28, pady=22, font="lucida 19 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b= Button(f,text="1",padx=28, pady=22, font="lucida 19 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack()


f.pack()
root.mainloop()