#This code creates a Tkinter window with a label "Price" and a horizontal slider to choose a value between 100 and 1000.
from tkinter import *

top = Tk()
top.geometry("300x200")

lbl = Label(top, text="Price", bg="yellow", fg="red")
lbl.pack()

scale = Scale(top, from_=100, to=1000, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

top.mainloop()
