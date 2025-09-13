from tkinter import *

parent = Tk()
parent.title("Students")
parent.geometry("300x200")

name = Label(parent, text="Name:")
name.grid(row=0, column=0, pady=10, padx=5)

c1 = Entry(parent)
c1.grid(row=0, column=1)

regno = Label(parent, text="Regd No.:")
regno.grid(row=1, column=0, pady=10, padx=5)

c2 = Entry(parent)
c2.grid(row=1, column=1)

btn = Button(parent, text="Submit")
btn.grid(row=3, column=1)

parent.mainloop()