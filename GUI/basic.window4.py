from tkinter import *

parent = Tk()
parent.title("Students")
parent.geometry("300x200")

name = Label(parent, text="Name :")
name.place(x=50, y=50)

c1 = Entry(parent)
c1.place(x=100, y=50)

regno = Label(parent, text="Regd No :")
regno.place(x=50, y=100)

c2 = Entry(parent)
c2.place(x=100, y=100)

#btn = Button(parent, text="Submit")
#btn.grid(row=3, column=1)

parent.mainloop()